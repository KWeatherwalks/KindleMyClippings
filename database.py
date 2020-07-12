import sqlite3

CREATE_NOTES_TABLE = "CREATE TABLE notes (id INTEGER PRIMARY KEY, title TEXT, edition TEXT author TEXT, note TEXT, page INTEGER, location TEXT, date DATE);"
INSERT_NOTE = "INSERT INTO notes (title, edition, author, note, page, location, date) VALUES (?,?,?,?,?,?,?);"
GET_ALL_NOTES = "SELECT * FROM notes;"
GET_ALL_NOTES_BY_AUTHOR = "SELECT * FROM notes WHERE author = ?;"
GET_ALL_NOTES_BY_TITLE = "SELECT * FROM notes WHERE title = ?;"


def connect():
    return sqlite3.connect("data.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_NOTES_TABLE)


def add_note(connection, title, edition, author, note, page, location, date):
    with connection:
        connection.execute(
            INSERT_NOTE, (title, edition, author, note, page, location, date)
        )


def get_all_notes(connection):
    with connection:
        return connection.execute(GET_ALL_NOTES).fetchall()


def get_notes_by_author(connection, author):
    with connection:
        return connection.execute(GET_ALL_NOTES_BY_AUTHOR, (author,)).fetchall()


def get_notes_by_title(connection, title):
    with connection:
        return connection.execute(GET_ALL_NOTES_BY_TITLE, (title,)).fetchall()
