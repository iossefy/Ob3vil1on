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
                elif choice == 'extract':
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
        self.arc = Archives()
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
            elif action == '--version':
                try:
                    var = sys.argv[2]
                    version.vManage(var)
                except Exception as e:
                    print("1 required arg missing!")
                    print("--current to get the current version")
                    print("--check to check for the latest version")
                    sys.exit(-1)
            elif action == '--extract':
                try:
                    self.option = sys.argv[2]
                    self.path = sys.argv[3]
                    self.password = sys.argv[4]
                    self.place = sys.argv[5]
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

    def arg_manager(self, option=None, path=None, password=None, place=None):
        if option == '--zip' or '--7z':
            try:
                self.extract_7z(path=path, password=password, place=place)
            except Exception as e:
                printer.unknowen_error(e)
                sys.exit(-1)
        if option == '--rar':
            try:
                self.extract_rar(path=path, password=password, place=place)
            except Exception as e:
                printer.unknowen_error(e)
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
