# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import os
import sys
sys.path.append('{path}'.format(path=os.getcwd()).replace('core/', ''))
import Obevilion


class Printer:
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
        ''')

        print("Coded By BL4CKvGHOST")
        print("%s" % Obevilion.get_name('all').upper())
        print("Updates: now officialy %s is the strongest Cracking Script" %
              Obevilion.get_name('all'))
        print("GitHub: https://github.com/BL4CKvGHOST")
        print("Twitter: https://twitter.com/BL4CKvGHOST")
        print("Usage: Python %s [display_mode] [archive path]" %
              Obevilion.get_name())
        print("Help!: python %s --help\n" % Obevilion.get_name())

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
        print("Inputing From Outside %s Shell" % Obevilion.get_name('all'))
        print('--gui:\t\tStart Graphical User Interface')
        print('--cli:\t\tStart Command Line Interface')
        print("--about\t\tAbout the app")
        print('--help:\t\tShow This Message\n')
        print("Inputing From Inside %s Shell" % Obevilion.get_name('all'))
        print("+=> BL4CKvGHOST\t\tShow Information About Me")
        print("+=> help\t\tShow This Message")
        print("+=> ifconfig\t\tShow You Local IP")
        print('+=> IP\t\t\tShow Your External IP')
        print("+=> License\t\tShow The License\n")
        print("How To Use?")
        print("EASY MODE:\tpython %s --easy_mode" % Obevilion.get_name())
        print(
            "CLI Example:\tpython %s --cli [Archive Path]" % Obevilion.get_name())
        print("GUI Example:\tpython %s --gui" % Obevilion.get_name())
        print("HELP EXAMPLE:\tpython %s --help\n" % Obevilion.get_name())

    def invalid_input(self):
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
       ''')

        print("%s" % Obevilion.get_name('all').upper())
        print("INVALID INPUT")
        print("Usage: Python %s [display_mode] [archive path]" %
              Obevilion.get_name())
        print("Help!: python %s --help" % Obevilion.get_name())

    def about(self):
        print('''
         █████╗ ██████╗  ██████╗ ██╗   ██╗████████╗
        ██╔══██╗██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝
        ███████║██████╔╝██║   ██║██║   ██║   ██║
        ██╔══██║██╔══██╗██║   ██║██║   ██║   ██║
        ██║  ██║██████╔╝╚██████╔╝╚██████╔╝   ██║
        ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝    ╚═╝
                                About {name}
        '''.format(name=Obevilion.get_name('all')))
        print('''
{name} is archive cracker tool, created in pure python.
{name} will be recreated in C soon for more experience while cracking,
{name} is supporting the latest version in python2 (Python 2.7.14).
{name} Have a gui interface for the user who cant deal with the cli.
{name} is designed for all Linux distributions.
with {name} you can crack [7z/zip/rar] files.
        '''.format(name=Obevilion.get_name('all')))

    def License(self):
        print('''
                      GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
         ''')

    def about_me(self):
        print('''
  ____  _    _  _    ____ _  __       ____ _   _  ___  ____ _____
 | __ )| |  | || |  / ___| |/ /_   __/ ___| | | |/ _ \/ ___|_   _|
 |  _ \| |  | || |_| |   | ' /\ \ / / |  _| |_| | | | \___ \ | |
 | |_) | |__|__   _| |___| . \ \ V /| |_| |  _  | |_| |___) || |
 |____/|_____| |_|  \____|_|\_\ \_/  \____|_| |_|\___/|____/ |_|

My real name is Youssef.
I'm a machine learning specialist and data analyst.
I’m a professional Python and Java developer with good knowledge and experience in C and Perl.

Twitter: https://twitter.com/BL4CKvGHOST
GitHub : https://github.com/BL4CKvGHOST
Reddit : https://reddit.com/u/BL4CKvGHOST
Website: https://bl4ckvghost.github.io

        ''')

    def unknowen_error(self, exception):
        print("Something went wrong!")
        print("\nStackTrace")
        print('{}\n'.format(exception))
        print(
            "You can report the error at https://github.com/BL4CKvGHOST/Obevilion/issues/")
        print('Exiting...')
