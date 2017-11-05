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

         print("OBEVILION")
         print("Updates: now officialy obevilion is the strongest Cracking Script")
         print("Coded By BL4CKvGHOST")
         print("GitHub: https://github.com/BL4CKvGHOST")
         print("Twitter: https://twitter.com/BL4CKvGHOST")
         print("Usage: Python %s [display_mode] [archive path]" % Obevilion.get_name())
         print("Help!: python %s --help" % Obevilion.get_name())

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

        print("OBEVILION")
        print("INVALID INPUT")
        print("Usage: Python %s [display_mode] [archive path]" % Obevilion.get_name())
        print("Help!: python %s --help" % Obevilion.get_name())
