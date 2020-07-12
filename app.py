import database

MENU_PROMPT = """-- Kindle My Clippings Notes App -- 

Please choose one of these options:

1) Upload a new My Clippings.txt file
2) See all notes
3) Find notes by author
4) Find notes by title
5) Exit

"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        print(user_input)

menu()
