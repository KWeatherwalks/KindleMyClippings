import re

import numpy as np
import pandas as pd
from unidecode import unidecode  # fixes issues with smart quotes

import database

#########################################################################################


def get_title_author(line):
    """Takes a string and returns a tuple containing the title, author, and edition
        if they match the title {collection} author format"""
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


def get_highlight_loc_date(line):
    """Takes a string and returns a tuple containing the page, location, and 
        date added if they match the pattern
    """
    try:
        page = re.search(highlight_pattern, line).group(1)
    except:
        page = None
        print("page ERROR")
    try:
        location = re.search(location_pattern, line).group(1)
    except:
        location = None
        print("location ERROR")
    try:
        date = re.search(date_pattern, line).group(1)
    except:
        date = None
        print("date ERROR")

    return page, location, date


def get_note(line):
    return unidecode(line).strip("\n")


#########################################################################################

# Regular expression patterns
title_author_pattern = re.compile(r"(\w+[^(]*) (\(.+\))?\s*\((.+)\)")
highlight_pattern = re.compile(r"page (\d+)")
location_pattern = re.compile(r"Location ([0-9-]+)")
date_pattern = re.compile(r"(\w{3,12} \d{1,2}, \d{4})")

#########################################################################################
def add_to_database(connection, filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        line = file.readline()
        line_count = 0
        while line:

            # Line 1: get the title and author name
            line = file.readline()
            if line:
                title, author, collection = get_title_author(line)
                line_count += 1

            # Line 2: the highlight, location, date added phase
            line2 = file.readline()
            if line2:
                page, location, date = get_highlight_loc_date(line2)
                line_count += 1

            # Line 3: blank
            line3 = file.readline()
            if line3:
                line_count += 1

            # Line 4: The note phase
            line4 = file.readline()
            if line4:
                note = get_note(line4)
                line_count += 1

            # Line 5: end of note
            line5 = file.readline()
            if line5:
                line_count += 1

            # print(
            #     "\nTitle:\t",
            #     title,
            #     "\nAuthor:\t",
            #     author,
            #     "\nEdition:\t",
            #     collection,
            #     "\nNote:\t",
            #     note,
            #     "\non page",
            #     page,
            #     "at location",
            #     location,
            #     "added on",
            #     date,
            # )
            # Add to database
            database.add_note(
                connection, title, collection, author, note, page, location, date
            )
    print(f"{line_count} lines read")


#########################################################################################
