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
        with open(output, 'a') as csv_file:
            write = csv.writer(csv_file, delimiter=',')
            write.writerow([str(fileName), str(password)])

    def read(self, output="core/configuration/output.csv"):
        """
        Reading the Information of the cracked files.
        output: not a required function, you can pass the csv file in there.
        """
        with open(output, 'rb') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                print("File Path: {filename}:\tPassword: {password}".format(
                    filename=line[0], password=line[1]))
                print("------------------------------------")

    def configuration(self, config='core/configuration/Settings.csv', UInput=None, line=None):
        """
        Reading the information in Settings.csv then
        Configure it with '--set' or 'set' commannd

        config: Configuration File Path
        """
        contents = []
        with open(config, 'r') as config_file:
            reader = csv.reader(config_file, delimiter=',')
            rows   = list(reader)
            contents.extend(rows)
        with open(config, 'w') as config_file:
            writer = csv.writer(contents, delimiter=',')
            if UInput != None:
                if line == 1:
                    contents[0][1] = str(UInput)
                    writer.writerow([contents[0][0], contents[0][1]])
                elif line == 2:
                    contents[1][1] = str(UInput)
                    writer.writerow([contents[1][0], contents[1][1]])
