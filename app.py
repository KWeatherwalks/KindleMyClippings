import database
from parse_myclippings import add_to_database

MENU_PROMPT = """-- Kindle My Clippings Notes App -- 

Please choose one of these options:

1) Upload a new My Clippings.txt file
2) See all notes
3) Find notes by author
4) Find notes by title
5) Reset database
6) Exit

Your selection: """


def menu():
    connection = database.connect()
    database.create_tables(connection)

    user_input = ""
    while user_input != "6":
        user_input = input(MENU_PROMPT)
        # Upload a new file
        if user_input == "1":
            filepath = input("Enter the full filepath: ")
            add_to_database(connection, filepath)
        # Show all notes
        elif user_input == "2":
            notes = database.get_all_notes(connection)
        # Show notes by author
        elif user_input == "3":
            pass
        # Show notes by title
        elif user_input == "4":
            pass
        # Reset database
        elif user_input == "5":
            reset = input("Are you sure? y/[n] ")
            if reset.lower() == "y":
                database.reset_database(connection)
        # Exit
        elif user_input == "6":
            connection.close()
            print("Goodbye!")
        # selection not on menu
        else:
            print("Invalid input, please try again!")

    connection.close()


menu()
