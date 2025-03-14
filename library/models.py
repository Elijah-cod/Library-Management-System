from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base  # Import Base from database.py

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    birth_date = Column(Date, nullable=False)
    nationality = Column(String, nullable=False)

    # One-to-Many Relationship
    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author(name={self.name}, nationality={self.nationality})>"

    @classmethod
    def create(cls, name, birth_date, nationality):
        session = get_db()  # Use the get_db() function to get a session
        try:
            # Convert birth_date from string to date object
            birth_date_obj = datetime.strptime(birth_date, "%Y-%m-%d").date()
            author = cls(name=name, birth_date=birth_date_obj, nationality=nationality)
            session.add(author)
            session.commit()
            print(f"Author '{name}' added successfully!")
        except Exception as e:
            session.rollback()
            print(f"Error creating author: {e}")
        finally:
            session.close()

    @classmethod
    def get_all(cls):
        session = get_db()
        try:
            return session.query(cls).all()
        finally:
            session.close()

    @classmethod
    def find_by_name(cls, name):
        session = get_db()
        try:
            return session.query(cls).filter_by(name=name).first()
        finally:
            session.close()

    @classmethod
    def delete(cls, name):
        session = get_db()
        try:
            author = cls.find_by_name(name)
            if author:
                session.delete(author)
                session.commit()
                print(f"Author '{name}' deleted successfully!")
            else:
                print("Author not found.")
        except Exception as e:
            session.rollback()
            print(f"Error deleting author: {e}")
        finally:
            session.close()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    publication_date = Column(Date)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    # Relationship to Author
    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"<Book(title={self.title}, genre={self.genre})>"

    @classmethod
    def create(cls, title, genre, publication_date, author_name):
        session = get_db()
        try:
            author = Author.find_by_name(author_name)
            if not author:
                print("Error: Author does not exist. Please add the author first.")
                return

            book = cls(title=title, genre=genre, publication_date=publication_date, author_id=author.id)
            session.add(book)
            session.commit()
            print(f"Book '{title}' added successfully!")
        except Exception as e:
            session.rollback()
            print(f"Error creating book: {e}")
        finally:
            session.close()

    @classmethod
    def get_all(cls):
        session = get_db()
        try:
            return session.query(cls).all()
        finally:
            session.close()

    @classmethod
    def find_by_title(cls, title):
        session = get_db()
        try:
            return session.query(cls).filter_by(title=title).first()
        finally:
            session.close()

    @classmethod
    def delete(cls, title):
        session = get_db()
        try:
            book = cls.find_by_title(title)
            if book:
                session.delete(book)
                session.commit()
                print(f"Book '{title}' deleted successfully!")
            else:
                print("Book not found.")
        except Exception as e:
            session.rollback()
            print(f"Error deleting book: {e}")
        finally:
            session.close()