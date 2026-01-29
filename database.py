from langchain_community.utilities import SQLDatabase

def get_db_connection():
    # Connect to local SQLite file
    db = SQLDatabase.from_uri("sqlite:///chinook.db")
    return db