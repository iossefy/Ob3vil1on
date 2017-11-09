# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import time
import sys
import Banner, gui, Obevilion
import subprocess

printer = Banner.Printer()

class LoopControl:
    """Looping In the terminal to let the user input
       without breaking the application."""
    def loop(self):
        choice = ""
        try:
            while choice != "exit":
                choice = raw_input("+=> ")
                if choice == 'gui':
                    gui.main()
                elif choice == 'cli':
                    print("DEBUGING") # Not Ready To Use Yet!, Just Debuging For Now
                elif choice == 'help':
                    printer.help_banner()
                elif choice == 'about':
                    printer.about()
                elif choice == '':
                    pass
                elif choice == 'exit':
                    print("Exiting...")
                    time.sleep(2)
                    sys.exit(1)
                elif choice == 'clear':
                    subprocess.call('clear', shell=True)
                elif choice == 'ifconfig':
                    subprocess.call('sudo ifconfig', shell=True)
                elif choice == 'ip':
                    subprocess.call('curl ifconfig.co')
                elif choice == 'license':
                    printer.License()
                elif choice == 'attacks':
                    print("CRACKING [ZIP, 7Z, RAR] FILES, AND MORE SOON...")
                elif choice == 'BL4CKvGHOST':
                    printer.about_me()
                else:
                    print("Invalid Input")
        except KeyboardInterrupt as ki:
            print('\nCtrl+C detected!')
            time.sleep(1)
            print("Exiting...")
            time.sleep(2)

class Attacks:
    """Managing the attacks from this class."""
    def __init__(self, arg):
        super(Attacks, self).__init__()
        self.arg = arg

class ConsoleColor:
    """Initializing Colors For The Text On The Console."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self, text=None, color=None):
        return "{color} {text} {end}".format(color=color, text=text, end=ENDC)
