import re

import numpy as np
import pandas as pd
from unidecode import unidecode


def get_title_author(title_author):
    """Takes a list containing a string with the title author pattern
        and returns a tuple containing the title and author"""
    if title_author:  # check that pattern was matched with line
        # if so, we are at the beginning of the entry
        title_author_string = title_author[0][:-1]
        title_author_list = title_author_string.split("(")
        title = title_author_list[0]
        author = title_author_list[-1]
        return title, author
    else:
        return None, None


def get_highlight_loc_date():
    pass


def get_note():
    pass


#########################################################################################
data_columns = ["title", "author", "note", "page", "location", "date_added"]
df = pd.DataFrame(columns=data_columns)

# <title> <(lastname, firstname)> pattern
title_author_pattern = re.compile(r".*\(\w+, \w+\)")

with open("My Clippings.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    line_count = 0
    while line:
        # The new entry phase

        # Line 1: get the title and author name
        try:
            title_author = title_author_pattern.findall(line)
            title, author = get_title_author(title_author)
            print(title, author)
        except ValueError:
            print("ERROR", title_author)
        except UnicodeError:
            print("error")

        # Line 2: the highlight, location, date added phase

        # Line 3: blank

        # Line 4: The note phase

        # Line 5: end of note
