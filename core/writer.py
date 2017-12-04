# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

"""
***WHAT IS THIS ALL ABOUT?***
Writing to the vault and reading to the vault.
it write file path, password, time to the vault.
where is the vault located?
its located at core/configuration/output.csv
"""

import csv
import time
from Banner import Printer

# Creating instance
printer = Printer()


class Booker(object):
    """docstring for Booker.

    ======================================
    |CREATING CSV FILES|READING CSV FILES |
    | :-------------   | :-------------   |
    |WRITING CSV FILES |DELETING CSV FILES|
    =======================================

    write: write to csv file.
    write argument:filename, password
    filename: pass the file name to write to file_name column in csv file
    password: pass the password to write to password column in csv file

    read: read the contents of the csv file.
    output: not a required function, you can pass the csv file in there

    """

    def write(self, fileName, password, output="core/configuration/output.csv"):
        """
        fileName: Getting the file name to write it into file_name column.
        password: Getting the Password to write it into password column.
        """
        try:
            # Append to the file
            with open(output, 'a') as csv_file:
                write = csv.writer(csv_file, delimiter=',')
                # Write filename then password then its time
                # Write the time in this format (Day/Month/Year Hour:Menute:Seconds)
                write.writerow([str(fileName), str(password), str(
                    time.strftime('%d/%m/%Y %H:%M:%S'))])
        except Exception as e:
            printer.unknowen_error(e)

    def read(self, output="core/configuration/output.csv"):
        """
        Reading the Information of the cracked files.
        output: not a required function, you can pass the csv file in there.
        """
        try:
            with open(output, 'rb') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for line in csv_reader:
                    # Read this columns
                    # Filename      Password        Time
                    print("File Path: {filename}\nPassword: {password}\nTime: {time}".format(
                        filename=line[0], password=line[1], time=line[2]))
                    print("------------------------------------")
        except Exception as e:
            printer.unknowen_error(e)
