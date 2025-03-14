from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    birth_date = Column(Date)
    nationality = Column(String)

    # One-to-Many Relationship
    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author(name={self.name}, nationality={self.nationality})>"


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