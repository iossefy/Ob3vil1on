# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import time
import sys
import Banner, gui, Obevilion

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
                else:
                    print("Invalid Input")
        except KeyboardInterrupt as ki:
            print('\nCTRL+C detected!')
            time.sleep(1)
            print("Exiting...")
            time.sleep(2)

class Attacks:
    """Managing the attacks from this class."""
    def __init__(self, arg):
        super(Attacks, self).__init__()
        self.arg = arg
