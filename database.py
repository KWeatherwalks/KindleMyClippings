import sqlite3

CREATE_NOTES_TABLE = "CREATE TABLE notes (id INTEGER PRIMARY KEY, title TEXT, author TEXT, note TEXT, page INTEGER, location TEXT, date DATE);"
INSERT_NOTE = "INSERT INTO notes (title, author, note, page, location, date) VALUES (?,?,?,?,?,?);"


def connect():
    return sqlite3.connect("data.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_NOTES_TABLE)


def add_note(connection, title, author, note, page, location, date):
    connection.execute(INSERT_NOTE, (title, author, note, page, location, date))
