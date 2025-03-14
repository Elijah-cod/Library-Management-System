# Library-Management-System
A simple CLI-based library management system that allows users to manage books and authors.

## Installation
To run this project, you need to have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

## Usage
To use this project, follow these steps:
1. Clone or fork the project from the GitHub repository: https://github.com/Elijah-cod/Library-Management-System to your local machine.
2. In your IDE terminal(VSCode) navigate to the project directory.
```bash
cd Library-Management-System
```
3. Install a virtual environment for this project
```bash
pipenv install
```
4. Open a subshell
```bash
pipenv shell
```
5. **cli.py** runs the interactive menu for the program. To start it, run the following command in the terminal:
```bash
python -m library.cli
```
## Classes
We used ORM to work with the Author and Book classes. In both classes, we implemented a method to retrieve all records, along with some CRUD operations like Create, Read, and Delete. We also added a method to find an author by name and a book by title.

## Database
We used Alembic and SQLAlchemy to track and update our database.
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite Database Connection
DATABASE_URL = "sqlite:///library.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    return SessionLocal()
```
## Cli
We designed an interactive system that allows users to choose a function to perform. We validate their choices, execute the selected function, and finalized it by ensuring a specific function runs only when the main menu is called.
```python
if __name__ == "__main__":
    main_menu()
```

