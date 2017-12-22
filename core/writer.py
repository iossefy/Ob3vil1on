# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import csv
import time
from Banner import Printer

# Creating instance
printer = Printer()


class OpenFile():
    """
    Setting up the context manager
    """

    def __init__(self, filename, mode):
        """
        filename: path of the file
        mode: mode to open the file with
        """
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        """Open the file"""
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        """Close the file"""
        self.file.close()


class Booker(object):
    """
    ======================================
    |CREATING CSV FILES|READING CSV FILES |
    | :-------------   | :-------------   |
    |WRITING CSV FILES |DELETING CSV FILES|
    =======================================

    This class read and write to the vault.

    whenever any password cracked it will be stored in the vault.
    the vault is located in {$PROJECT}/core/configuration/output.csv.

    Methods
    read: read the contents of the csv file.
    output: not a required function, you can pass the csv file in there

    Methods Parameters
    write: write to csv file.
    write argument:filename, password
    filename: pass the file name to write to file_name column in csv file
    password: pass the password to write to password column in csv file
    """

    def write(self, fileName, password, output="core/configuration/output.csv"):
        """
        fileName: Getting the file name to write it into file_name column.
        password: Getting the Password to write it into password column.
        """
        try:
            # Append to the file
            with OpenFile(output, 'a') as csv_file:
                write = csv.writer(csv_file, delimiter=',')
                # Write filename then password then its time
                # Write the time in this format (Day/Month/Year Hour:Menute:Seconds)
                write.writerow([str(fileName), str(password), str(
                    time.strftime('%d/%m/%Y %H:%M:%S'))])
        except Exception as e:
            printer.unknowen_error(e)

    def read(self, output="core/configuration/output.csv"):
        """
        Reading output file.
        reading this in this format

        ######################
        File Path: {$filepath}
        Password: {$pwd}
        Time: {$time}
        ######################

        Methods:
        Reading the Information of the cracked files.
        output: not a required function, you can pass the csv file in there.
        """
        try:
            with OpenFile(output, 'rb') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for line in csv_reader:
                    # Read this columns
                    # Filename      Password        Time
                    print("File Path: {filename}\nPassword: {password}\nTime: {time}".format(
                        filename=line[0], password=line[1], time=line[2]))
                    print("------------------------------------")
        except Exception as e:
            printer.unknowen_error(e)
