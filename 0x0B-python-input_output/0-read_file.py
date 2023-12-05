#!/usr/bin/python3

"""
Write a function that reads a text file (UTF8) and prints it to stdout
"""

def read_file(filename=""):
    with open(finlename, "r", encoding="UTF-8") as file:
        print(file.read(), end="")
