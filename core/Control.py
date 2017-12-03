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
from version import VControl

# Creating instances for classes
version = VControl()
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
            # While loop to loop in user input
            while choice != "exit":
                choice = raw_input("+=> ") # Pointer XD
                if choice == 'gui':
                    gui.main() # Start GUI Window
                elif choice == 'cli':
                    self.attacks.cli_bruteforce_attack() # Start cli attack
                elif choice == 'help': # print help
                    printer.help_banner()
                elif choice == 'about':
                    printer.about() # print about
                elif choice == '': # Just Pass :)
                    pass
                elif choice == 'extract':
                    print("Not Available Right Now!")
                elif choice == 'exit':
                    # Exit From easy_mode
                    print("Exiting...")
                    time.sleep(2)
                    sys.exit(1)
                elif choice == 'clear':
                    subprocess.call('clear', shell=True) # Clear the terminal
                elif choice == 'license':
                    printer.License() # print the license
                elif choice == 'attacks':
                    print("CRACKING [ZIP, 7Z, RAR] FILES, AND MORE SOON...")
                elif choice == "vault":
                    booker.read() # read from the vault
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
        # Creating instances
        self.attacks = Attacks()
        self.arc = Archives()
        try:
            assert action in commands, "Action is not one of %s" % ', '.join(
                map(str, commands))
            try:
                # Setting up --easy_mode
                if action == '--easy_mode':
                    subprocess.call('clear', shell=True)
                    printer.main_banner() # print the main banner
                    self.loop() # loop in terminal
                else:
                    pass
            except Exception as e:
                pass
            if action == '--gui':
                gui.main() # Open GUI Window
            elif action == '--cli':
                try:
                    # Setting up the args
                    self.temp = sys.argv[2]
                    self.attacks.manage_args()
                except Exception as e:
                    print(
                        'choose another argument\n-b\tfor bruteforce attack\n-d\tfor dictionary attack')
            elif action == '--help':
                printer.help_banner() # print help banner
            elif action == '--about':
                printer.about() # Print about
            elif action == '--about_me':
                printer.about_me() # Print about me
            elif action == '--license':
                printer.License() # print the license
            elif action == '--vault':
                booker.read() # Read from the vault
            elif action == '--version':
                try:
                    # Setting up args
                    var = sys.argv[2]
                    # Run this method
                    version.vManage(var)
                except Exception as e:
                    print("1 required arg missing!")
                    print("--current to get the current version")
                    print("--check to check for the latest version")
                    sys.exit(-1)
            elif action == '--extract':
                try:
                    # Required Arguments for --extract command
                    self.option = sys.argv[2]       # File Type
                    self.path = sys.argv[3]         # file path
                    self.password = sys.argv[4]     # file password
                    self.place = sys.argv[5]        # extract place
                    try:
                        self.arc.arg_manager(option=self.option, path=self.path, password=self.password, place=self.place)
                    except Exception as e:
                        printer.unknowen_error(e)
                except Exception as e:
                    print("Something went wrong!")
                    print("Try: python Obevilion.py [option] [path] [password] [place]")
                    print("i.e python Obevilion.py --zip /path/to/archive.zip S3CR3T /place/to/extract")
                    print("try in order!")
                    sys.exit(-1)
            elif action == '--attacks':
                print("CRACKING [ZIP, 7Z, RAR] FILES AND MORE SOON...")
        except Exception as e:
            try:
                # If the user input invalid command
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
            if path != '':# if path not equal blank
                subprocess.call(
                    'python3 core/model.py {file}'.format(file=path), shell=True)
            else:
                print("Try Again!")
        except Exception as e:
            printer.unknowen_error(e)
            time.sleep(2)
            sys.exit(1)

    def cli_bruteforce_attack_outshell(self):
        """
        BruteForce Attack in the external shell [Terminal Arguments]
        """
        try:
            # path is set to user input at the third arg
            path = sys.argv[3]
            if path == '' or path is None: # if the user enter nothing
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
            # path is set to user input at the third arg
            path = sys.argv[3]
            if path == '' or path is None: # if the user enter nothing
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

            '-d' '--dictionary' is for dictionary attack
            '-b' '--bruteforce' is for bruteforce attack

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
            # Set attack type to the second arg in terminal
            self.arg = sys.argv[2]
            # if second arg = '-b' or '--bruteforce' start bruteforce attack
            if self.arg == "-b" or self.arg == '--bruteforce':
                self.cli_bruteforce_attack_outshell()
            elif self.arg == '-d' or self.arg == '--dictionary':
            # if second arg = 'd' or '--dictionary' start dictionary attack
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
       extract_rar: extract rar files.
       extract_7z: extract 7z and zip files.."""

    def arg_manager(self, option=None, path=None, password=None, place=None):
        if option == '--zip' or '--7z': # if the file type equal zip or 7z
            try:
                # Start extracting file
                self.extract_7z(path=path, password=password, place=place)
            except Exception as e:
                printer.unknowen_error(e) # print the error
                sys.exit(-1)
        if option == '--rar': # if the file type equal zip or 7z
            try:
                # Start extracting file
                self.extract_rar(path=path, password=password, place=place)
            except Exception as e:
                printer.unknowen_error(e) # print the error
                sys.exit(-1)

    def extract_rar(self, path=None, password=None, place=None):
        """Extracting rar files using subprocess."""
        try:
            subprocess.call("unrar x -p{pwd} {filename} {dist}".format(
                pwd=password, filename=path, dist=place), shell=True)
        except Exception as e:
            printer.unknowen_error(e)

    def extract_7z(self, path=None, password=None, place=None):
        """Extract 7z files using subprocess."""
        try:
            subprocess.call("7z x {filename} -o{dist} -p{pwd}".format(
                pwd=password, filename=path, dist=place), shell=True)
        except Exception as e:
            printer.unknowen_error(e)
