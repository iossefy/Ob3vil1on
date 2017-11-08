# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

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
         print("Updates: now officialy %s is the strongest Cracking Script" % Obevilion.get_name('all'))
         print("GitHub: https://github.com/BL4CKvGHOST")
         print("Twitter: https://twitter.com/BL4CKvGHOST")
         print("Usage: Python %s [display_mode] [archive path]" % Obevilion.get_name())
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

        print('--gui:\t\tStart Graphical User Interface')
        print('--cli:\t\tStart Command Line Interface')
        print('--help:\t\tShow This Message\n')
        print("CLI Example:\tpython %s --cli [Archive Path]" % Obevilion.get_name())
        print("GUI Example:\tpython %s --gui" % Obevilion.get_name())
        print("HELP EXAMPLE:\tpython %s --help" % Obevilion.get_name())

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
        print("Usage: Python %s [display_mode] [archive path]" % Obevilion.get_name())
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
