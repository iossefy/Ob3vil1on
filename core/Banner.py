# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import os
import sys

name = "Obevilion.py"

class Printer(object):
    """Just Printing Banners in this class."""

    def main_banner(self):
        print('''

        ████▄ ███   ▄███▄      ▄   ▄█ █    ▄█ ████▄    ▄
        █   █ █  █  █▀   ▀      █  ██ █    ██ █   █     █
        █   █ █ ▀ ▄ ██▄▄   █     █ ██ █    ██ █   █ ██   █
        ▀████ █  ▄▀ █▄   ▄▀ █    █ ▐█ ███▄ ▐█ ▀████ █ █  █
              ███   ▀███▀    █  █   ▐     ▀ ▐       █  █ █
                              █▐                    █   ██
                              ▐
                                   NO ONE WILL GIVE YOU FREEDOM
                                   YOU TAKE IT!

            Created By: BL4CKvGHOST<youssefheshamhassan@gmail.com>
            Code Name: CoXZ
        ''')

        print("Coded By BL4CKvGHOST")
        print("{}".format(name[:-3]))
        print("Updates: now officialy {} is the strongest Cracking Script".format(name[:-3]))
        print("GitHub: https://github.com/BL4CKvGHOST")
        print("Twitter: https://twitter.com/BL4CKvGHOST")
        print("Usage: Python {} [display_mode] [archive path]".format(name))
        print("Help!: python {} --help\n".format(name))

    def help_banner(self):
        print('''
           ▄█    █▄       ▄████████  ▄█          ▄███████▄
          ███    ███     ███    ███ ███         ███    ███
          ███    ███     ███    █▀  ███         ███    ███
         ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███         ███    ███
        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ▀█████████▀
          ███    ███     ███    █▄  ███         ███
          ███    ███     ███    ███ ███▌    ▄   ███
          ███    █▀      ██████████ █████▄▄██  ▄████▀
                                    ▀

                          Need Help?
  ============================================================
        ''')
        print("Inputing From Outside {} Shell".format(name[:-3]))
        print('--gui:\t\t\tStart Graphical User Interface')
        print('--cli:\t\t\tStart Command Line Interface')
        print("\t\t\tUSAGE: --cli [argument]")
        print("\t\t\t-b  --bruteforce [file path]")
        print("\t\t\t-d  --dictionary [file path]")
        print("--about\t\t\tAbout the app")
        print("--attacks\t\tShow available attacks")
        print("--license\t\tShow license")
        print("--vault\t\t\tShow Cracked Files names and password")
        print('--help:\t\t\tShow This Message\n')
        print("--version\t\tShow The Current Version")
        print("\t\t\tUSAGE:--version [argument]")
        print("\t\t\t--current\t get the current version")
        print("\t\t\t--check\t check for updates")
        print("--extract\t\tExtract Archive")
        print("\t\t\tUSAGE: --extract [file type] [file path] [file password] [place to store]\n")
        print("Inputing From Inside {} Shell".format(name))
        print("+=> extract\t\tExtract Archive")
        print("+=> help\t\tShow This Message")
        print("+=> license\t\tShow The License")
        print("+=> clear\t\tClear The Screen")
        print("+=> attacks\t\tShow available attacks")
        print("+=> vault\t\tShow File names and passwords\n")
        print("How To Use?")
        print("EASY MODE:\t\tpython {} --easy_mode".format(name))
        print(
            "CLI MODE:\t\tpython {} --cli [Attack Mode] [Archive Path]".format(name))
        print("GUI MODE:\t\tpython {} --gui".format(name))
        print("HELP SCREEN:\t\tpython {} --help\n".format(name))

    def invalid_input(self, uinput=None):
        if uinput!=None:
            print("Invalid Input {}".format(uinput))
        else:
            print("Invalid Input")
        print("Help!: python {} --help".format(name))

    def about(self):
        print('''
         █████╗ ██████╗  ██████╗ ██╗   ██╗████████╗
        ██╔══██╗██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝
        ███████║██████╔╝██║   ██║██║   ██║   ██║
        ██╔══██║██╔══██╗██║   ██║██║   ██║   ██║
        ██║  ██║██████╔╝╚██████╔╝╚██████╔╝   ██║
        ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝    ╚═╝
                                About Obevilion
        ''')
        print('''
{n} is archive cracker tool, created in pure python.
{n} will be recreated in C soon for more experience while cracking,
{n} is supporting the latest version in python2 (Python 2.7.14).
{n} Have a gui interface for the user who cant deal with the cli.
{n} is designed for all Linux distributions.
with Obevilion you can crack [7z/zip/rar] files.
        '''.format(n=name[:-3]))

    def License(self):
        print('''
                      GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
         ''')

    def unknowen_error(self, exception, whatever=None):
        print("Something went wrong!")
        if whatever == None:
            pass
        else:
            print('{}'.format(whatever))
        print("\nStackTrace")
        print('{}\n'.format(exception))
        print(
            "You can report the error at https://github.com/BL4CKvGHOST/issues/")
        print('Exiting...')

    def extract_err(self):
        print("Something went wrong!")
        print("Try: python Obevilion.py [option] [path] [password] [place]")
        print("i.e python Obevilion.py --zip /path/to/archive.zip S3CR3T /place/to/extract")
        print("try in order!")

    def version_err(self):
        print("1 required arg missing!")
        print("--current to get the current version")
        print("--check to check for the latest version")

    def attacks(self):
        print("CRACKING [ZIP, 7Z, RAR] FILES...")
        print("CLI AND GUI ATTACKS AVAILABLE TO YOU!")
        print("BRUTEFORCE/DICTIONARY ATTACKS")
