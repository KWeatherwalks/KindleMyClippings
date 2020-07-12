import re

import numpy as np
import pandas as pd

# from unidecode import unidecode


def get_title_author(line):
    """Takes a string and returns a tuple containing the title and author
        if they match the title author format"""
    try:
        title_author = re.search(title_author_pattern, line)
    except ValueError:
        print("Value ERROR", title_author)
    except UnicodeError:
        print("Unicode ERROR")

    title = title_author.group(1)
    author = title_author.group(3)
    collection = title_author.group(2)
    if collection:
        collection = collection.strip("()")

    return title, author, collection


def get_highlight_loc_date():
    pass


def get_note():
    pass


#########################################################################################
data_columns = ["title", "author", "note", "page", "location", "date_added"]
df = pd.DataFrame(columns=data_columns)

# <title> <(lastname, firstname)> pattern
title_author_pattern = re.compile(r"(\w+[^(]*) (\(.+\))?\s*\((.+)\)")

with open("My Clippings.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    line_count = 0
    while line:
        # The new entry phase

        # Line 1: get the title and author name
        line = file.readline()
        if line:
            print("\nReading line 1: {0}".format(line), end="")
            title, author, collection = get_title_author(line)
            line_count += 1

        # Line 2: the highlight, location, date added phase
        line2 = file.readline()
        if line2:
            print("Reading line 2: {0}".format(line2))
            line_count += 1

        # Line 3: blank
        line3 = file.readline()
        if line3:
            # print("Reading line 3: {0}".format(line3))
            line_count += 1

        # Line 4: The note phase
        line4 = file.readline()
        if line4:
            # print("Reading line 4: {0}".format(line4))
            line_count += 1

        # Line 5: end of note
        line5 = file.readline()
        if line5:
            # print("Reading line 5: {0}".format(line5))
            line_count += 1

        print("Title:\t", title, "\nAuthor:\t", author, "\nEdition:\t", collection)

print(f"{line_count} lines read")
