# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import time
import sys
from Banner import Printer
from UI import gui
import subprocess
from writer import Booker

printer = Printer()
booker = Booker()


class LoopControl(object):
    """
    Looping In the terminal to let the user input
    without breaking the application.
    """

    def loop(self):
        """
        Looping throgh user input
        """
        self.attacks = Attacks()
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
                    subprocess.call('curl ifconfig.co', shell=True)
                elif choice == 'license':
                    printer.License()
                elif choice == 'attacks':
                    print("CRACKING [ZIP, 7Z, RAR] FILES, AND MORE SOON...")
                elif choice == "vault":
                    booker.read()
                elif choice == 'BL4CKvGHOST':
                    printer.about_me()
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
                self.attacks.manage_args()
            elif action == '--help':
                printer.help_banner()
            elif action == '--about':
                printer.about()
            elif action == '--about_me':
                printer.about_me()
            elif action == '--license':
                printer.License()
            elif action == '--vault':
                booker.read()
            elif action == '--set':
                pass #
            elif action == '--attacks':
                print("CRACKING [ZIP, 7Z, RAR] FILES AND MORE SOON...")
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
        BruteForce Attack in the external shell [Terminal Arguments]
        """
        try:
            path = sys.argv[3]
            if path == '' or path is None:
                print("Try Again!")
            else:
                subprocess.call(
                    'python3 core/model.py {file}'.format(file=path), shell=True)
        except Exception as e:
            printer.unknowen_error(exception=e)
            time.sleep(2)
            sys.exit(1)

    def cli_dictionary_attack_outshell(self):
        """
        Dictionary Attack in the external shell [Terminal Arguments]
        """
        try:
            path = sys.argv[3]
            if path == '' or path is None:
                print("There Is 1 arg Messing")
            else:
                print("Use BruteForce Attack\nTrust Me Its Better")
        except Exception as e:
            printer.unknowen_error(exception=e)
            time.sleep(2)
            sys.exit(1)

    def manage_args(self):
        try:
            self.arg = sys.argv[2]
            if self.arg == "-b":
                self.cli_bruteforce_attack_outshell()
            elif self.arg == '-d':
                self.cli_dictionary_attack_outshell()
        except Exception as e:
            pass

class Settings(object):
    """
    docstring for Settings.
    Managing The Passwords,
    inputs and outputs of the configuration folder.
    """
    def __init__(self):
        pass

    def set_command(self, command):
        try:
            command = sys.argv[1]
        except Exception as e:
            raise
