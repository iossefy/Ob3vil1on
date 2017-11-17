# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import csv


class Booker(object):
    """docstring for Booker.

    ======================================
    |CREATING CSV FILES|READING CSV FILES |
    | :-------------   | :-------------   |
    |WRITING CSV FILES |DELETING CSV FILES|
    =======================================

    """

    def write(self, fileName, password):
        """
        fileName: Getting the file name to write it into file_name column.
        password: Getting the Password to write it into password column.
        """
        with open("output.csv", 'a') as csv_file:
            write = csv.writer(csv_file)
            write.withrow([fileName, password])

    def read(self):
        """Reading the Information of the cracked files."""
        with open("output.csv", 'r') as csv_file:
            csv_reader = csv.read(csv_file)
            for line in csv_reader:
                print("{filename}:{password}".format(line[0], line[1]))
