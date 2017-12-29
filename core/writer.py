# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import csv
import time
import os
import re
import sys
import colorama
from Banner import Printer

# Creating instance
printer = Printer()


class OpenFile(object):
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


PY3 = sys.version_info[0] >= 3

__all__ = (
    'red', 'green', 'yellow', 'blue',
    'black', 'magenta', 'cyan', 'white',
    'clean', 'disable'
)

COLORS = __all__[:-2]

if 'get_ipython' in dir():
    """
       when ipython is fired lot of variables like _oh, etc are used.
       There are so many ways to find current python interpreter is ipython.
       get_ipython is easiest is most appealing for readers to understand.
    """
    DISABLE_COLOR = True
else:
    DISABLE_COLOR = False


class ColoredString(object):  # code from https://github.com/kennethreitz/crayons
    """Enhanced string for __len__ operations on Colored output."""

    def __init__(self, color, s, always_color=False, bold=False):
        super(ColoredString, self).__init__()
        if not PY3 and isinstance(s, unicode):
            self.s = s.encode('utf-8')
        else:
            self.s = s
        self.color = color
        self.always_color = always_color
        self.bold = bold
        if os.environ.get('CLINT_FORCE_COLOR'):
            self.always_color = True

    def __getattr__(self, att):
        def func_help(*args, **kwargs):
            result = getattr(self.s, att)(*args, **kwargs)
            try:
                is_result_string = isinstance(result, basestring)
            except NameError:
                is_result_string = isinstance(result, str)
            if is_result_string:
                return self._new(result)
            elif isinstance(result, list):
                return [self._new(x) for x in result]
            else:
                return result
        return func_help

    @property
    def color_str(self):
        style = 'BRIGHT' if self.bold else 'NORMAL'
        c = '%s%s%s%s%s' % (getattr(colorama.Fore, self.color), getattr(
            colorama.Style, style), self.s, colorama.Fore.RESET, getattr(colorama.Style, 'NORMAL'))

        if self.always_color:
            return c
        elif sys.stdout.isatty() and not DISABLE_COLOR:
            return c
        else:
            return self.s

    def __len__(self):
        return len(self.s)

    def __repr__(self):
        return "<%s-string: '%s'>" % (self.color, self.s)

    def __unicode__(self):
        value = self.color_str
        if isinstance(value, bytes):
            return value.decode('utf8')
        return value

    if PY3:
        __str__ = __unicode__
    else:
        def __str__(self):
            return self.color_str

    def __iter__(self):
        return iter(self.color_str)

    def __add__(self, other):
        return str(self.color_str) + str(other)

    def __radd__(self, other):
        return str(other) + str(self.color_str)

    def __mul__(self, other):
        return (self.color_str * other)

    def _new(self, s):
        return ColoredString(self.color, s)


def clean(s):
    strip = re.compile(
        "([^-_a-zA-Z0-9!@#%&=,/'\";:~`\$\^\*\(\)\+\[\]\.\{\}\|\?\<\>\\]+|[^\s]+)")
    txt = strip.sub('', str(s))
    strip = re.compile(r'\[\d+m')
    txt = strip.sub('', txt)
    return txt

# Return Colors


def black(string, always=False, bold=False):
    return ColoredString('BLACK', string, always_color=always, bold=bold)


def red(string, always=False, bold=False):
    return ColoredString('RED', string, always_color=always, bold=bold)


def green(string, always=False, bold=False):
    return ColoredString('GREEN', string, always_color=always, bold=bold)


def yellow(string, always=False, bold=False):
    return ColoredString('YELLOW', string, always_color=always, bold=bold)


def blue(string, always=False, bold=False):
    return ColoredString('BLUE', string, always_color=always, bold=bold)


def magenta(string, always=False, bold=False):
    return ColoredString('MAGENTA', string, always_color=always, bold=bold)


def cyan(string, always=False, bold=False):
    return ColoredString('CYAN', string, always_color=always, bold=bold)


def white(string, always=False, bold=False):
    return ColoredString('WHITE', string, always_color=always, bold=bold)


def disable():
    """Disables colors."""
    global DISABLE_COLOR

    DISABLE_COLOR = True
