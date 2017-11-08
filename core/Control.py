# -*- coding: utf-8 -*-
import time
import sys
import Banner, gui, Obevilion

printer = Banner.Printer()

class LoopControl:
    """Looping In the terminal to let the user input
       without breaking the application."""
    def loop(self):
        choice = ""
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
