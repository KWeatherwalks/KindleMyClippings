import database
import main

MENU_PROMPT = """-- Kindle My Clippings Notes App -- 

Please choose one of these options:

1) Upload a new My Clippings.txt file
2) See all notes
3) Find notes by author
4) Find notes by title
5) Exit


Your selection: """


def menu():
    connection = database.connect()
    database.create_tables(connection)

    user_input = ""
    while user_input != "5":
        user_input = input(MENU_PROMPT)
        if user_input == "1":
            filepath = input("Enter the full filepath: ")
            main.add_to_database(connection, filepath)
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            pass
        else:
            print("Invalid input, please try again!")


menu()
