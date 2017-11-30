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
                elif: choice == 'extract':
                    print("Not Available Right Now!")
                elif choice == 'exit':
                    print("Exiting...")
                    time.sleep(2)
                    sys.exit(1)
                elif choice == 'clear':
                    subprocess.call('clear', shell=True)
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
                try:
                    self.temp = sys.argv[2]
                    self.attacks.manage_args()
                except Exception as e:
                    print(
                        'choose another argument\n-b\tfor bruteforce attack\n-d\tfor dictionary attack')
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
            elif action == '--extract':
                print("Not Available Right Now!")
            elif action == 'BL4CKvGHOST':
                printer.about_me()
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
        """
        Managing the args that the user enters
        if the user enter [obevilion.py --cli (attack type)]
        this method is managing the (attack type) place in the previews ex.

        Parameters:

            '-d' is for dictionary attack
            '-b' is for bruteforce attack

        if the user enter '-b'
        the user will be using bruteforce attack and this method will direct
        the user to this method 'cli_bruteforce_attack_outshell'.

        if the user enter '-d'
        the user will be using bruteforce attack and this method will direct
        the user to this method 'cli_bruteforce_attack_outshell'.

        otherwise, it will print 'Invalid argument: ' and the argument that
        the user miss typed.

        """
        try:
            self.arg = sys.argv[2]
            if self.arg == "-b":
                self.cli_bruteforce_attack_outshell()
            elif self.arg == '-d':
                self.cli_dictionary_attack_outshell()
            else:
                print("Invalid argument: {}".format(self.arg))
        except Exception as e:
            pass


class Archives(object):
    """docstring for Archives.
       Managing extarcting archive
       files.

       Methods:
       extract_zip: extract zip files.
       extract_rar: extract rar files.
       extract_7z: extract 7z files.
       EXTRACT: the manager."""

    def arg_manager(self, option):
        """
        Managing the args.
        (i.e. Obevilion.py extract zip /path/to/file.zip)
        """
        pass

    def EXTRACT(self, file_type=None, file_name=None, password=None, place=None):
        if password == '' or password is None:
            print("Extracting with passwords only!")
        if distination == '' or distination is None:
            print("Enter a place to store the extracted files")
        if path == '' or path is None:
            print("Enter the archive path")

        # Initializing the variables to be used in other methods
        self.file_type = file_type
        self.file_name = file_name
        self.password  = password
        self.place     = place

        # Checking the file type
        if file_type == "zip":
            pass
        elif file_type == "rar":
            pass
        elif file_type == "7z":
            pass

        # Setting up the variables that will be used in extracting process
        self.ex_rar = 'unrar x -p{pwd} {name} {distination}'.format(
            pwd=password, name=file_name, distination=place)
        self.ex_7z = '7za t -p{pwd} {filename} {distination}'.format(
            pwd=password, filename=file_name, distination=place)
        self.ex_zip = 'unzip {filename} -P{pwd} {distination}'.format(
            pwd=password, filename=file_name, distination=place)

    def extract_zip(self, path=None, password=None, place=None):
        """Extracting zip files."""
        pass

    def extract_rar(self, path=None, password=None, place=None):
        """Extracting rar files."""
        pass

    def extract_7z(self, path, password=None, place=None):
        """Extract 7z files."""
        pass
