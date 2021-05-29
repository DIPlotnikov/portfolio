#!/usr/bin/python3
# -*- coding: utf-8 -*-

# A class for easy working with files. Practice magic methods.

# D.Plotnikov 2021

import os.path
import tempfile


class File:
    """
    A class for working with files.
    Initializing the class creates a file for further work.
    When creating a class object, specify the file name.
    The file is created in the same directory where the program is located.
    The write() and read() functions allow you to write
    and read information from a file.
    """

    def __init__(self, filename):
        self.name = filename
        if not os.path.exists(filename):
            with open(self.name, "w"):
                pass

    def __str__(self):
        return os.path.abspath(self.name)

    def __add__(self, other):
        storage_path = tempfile.NamedTemporaryFile().name
        f = File(storage_path)
        f.write(self.read() + other.read())
        return f

    def __iter__(self):
        self.read_file = open(self.name, "r")
        return self.read_file

    def read(self):
        with open(self.name, "r") as read_file:
            return read_file.read()

    def write(self, text):
        with open(self.name, "w") as write_file:
            write_file.write(text)

    def __exit__(self):
        self.read_file.close()


