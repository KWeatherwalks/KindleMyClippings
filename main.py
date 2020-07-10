import re

import numpy as np
import pandas as pd

df = pd.DataFrame(columns=["title", "author", "note", "page", "location", "date_added"])


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


# <title> <(lastname, firstname)> pattern
title_author_pattern = re.compile(r".*\(\w+, \w+\)")
state = 0  # 3 states: new (0), second (1), note (2)
with open("My Clippings.txt", "r", encoding="utf-8") as file:
    for line in file:
        # check to see if all data has been collected for the current entry
        if line == "==========":
            # do something to submit the entry and reset the data

            state = 0
            continue  # bypass the remaining checks

        # The new entry state
        elif state == 0:
            # get the title and author data
            data = [None for _ in range(len(df.columns))]
            # get the title and author name
            try:
                title_author = title_author_pattern.findall(line)
                title, author = get_title_author(title_author)
            except ValueError:
                print("ERROR", title_author)
            except UnicodeError:
                print("error")
            # move to next state
            state += 1

        # The highlight, location, date added phase
        elif state == 1:
            # do something to get the data

            # move to next state
            state += 1

        # The note phase
        elif state == 2:
            pass
