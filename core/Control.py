# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import time
import sys
import Banner
from UI import gui
import subprocess
from writer import Booker

printer = Banner.Printer()


class LoopControl:
    """Looping In the terminal to let the user input
       without breaking the application."""

    def loop(self):
        """
        Looping throgh user input
        """
        self.attacks = Attacks()
        self.reader = Booker().read()
        choice = ""
        try:
            while choice != "exit":
                choice = raw_input("+=> ")
                if choice == 'gui':
                    gui.main()
                elif choice == 'cli':
                    self.attacks.cli_bruteforce_attack()
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
                elif choice == "show database":
                    self.reader()
                else:
                    print("Invalid Input")
        except KeyboardInterrupt as ki:
            print('\nCtrl+C detected!')
            time.sleep(1)
            print("Exiting...")
            time.sleep(2)

    def main_loop(self, action=None, commands=None):
        """
        Script Main Loop
        """
        self.attacks = Attacks()
        try:
            assert action in commands, "Action is not one of %s" % ', '.join(
                map(str, commands))
            try:
                if action == '--easy_mode':
                    subprocess.call('clear', shell=True)
                    printer.main_banner()
                    self.loop()
                else:
                    pass
            except Exception as e:
                pass
            if action == '--gui':
                gui.main()
            elif action == '--cli':
                self.attacks.cli_bruteforce_attack_outshell()
            elif action == '--help':
                printer.help_banner()
            elif action == '--about':
                printer.about()
            elif action == '--about_me':
                printer.about_me()
            elif action == '--license':
                printer.License()
        except Exception as e:
            try:
                if sys.argv[1] is not commands:
                    printer.invalid_input()
                else:
                    pass
            except Exception as e:
                pass


class Attacks:
    """
    Managing the attacks from this class.
    This class will manage all kinds of
    attacks including bruteforce attack and
    dictionary attack. this class will manage both
    [Command Line Interface / Graphical User Interface] Attacks.
    """

    def cli_bruteforce_attack(self):
        """
        Attacking inside [the easy mode]
        """
        try:
            path = raw_input('path:')
            if path != '':
                subprocess.call(
                    'python3 core/model.py {file}'.format(file=path), shell=True)
            else:
                print("Try Again!")
        except Exception as e:
            printer.unknowen_error(exception=e)
            time.sleep(2)
            sys.exit(1)

    def cli_bruteforce_attack_outshell(self):
        """
        Attacking in the external shell [Terminal Argu]
        """
        try:
            path = sys.argv[2]
            if path == '' or path  None:
                print("Try Again!")
            else:
                subprocess.call(
                    'python3 core/model.py {file}'.format(file=path), shell=True)
        except Exception as e:
            printer.unknowen_error(exception=e)
            time.sleep(2)
            sys.exit(1)
