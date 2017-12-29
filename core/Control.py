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
import writer
from writer import Booker
from version import VControl
from configuration import settings

# Creating instances for classes
version = VControl()
printer = Printer()
booker = Booker()


class LoopControl(object):
    """
    Looping In the terminal to let the user input
    without breaking the application.

    Methods:
    __init__: Initializing Variables
    loop: easy_mode loop
    main_loop: the main loop of the scripts
    show_set: show the configuration as a python list
    noob_conf: settings configuration in easy_mode
    pro_conf: settings configuration in command line arguments mode
    framework_settings: setting up the framework settings
    uid_settings: setting up the uid settings
    """
    def __init__(self):
        """
        Creating some instances and Initializing some variables
        """
        self.attacks = Attacks()
        self.arc = Archives()

    def loop(self):
        """
        Looping throgh user input.
        Console will be somthing like that

        ====================================
        = Obevilion                        =
        = Version                          =
        = Startup commands                 =
        = +=>                              =
        ====================================

        this is the loop for easy mode prompt
        easy mode prompt is [easy] for noob users
        easy mode is a simple mode to use instead of
        entering command line arguments.
        it will loop with this prompt '+=>' until the user
        enters a valid command; if the command is valid,
        go execute what in it.
        if not just print("Invalid Input").
        if the user press 'CTRL+C' exit.
        """
        choice = ""
        try:
            # While loop to loop in user input
            while choice != "exit":
                choice = raw_input(writer.blue("+=> ", bold=True))  # Pointer
                if choice == 'gui':
                    gui.main()  # Start GUI Window
                elif choice == 'cli':
                    self.attacks.cli_bruteforce_attack()  # Start cli attack
                elif choice == 'help':  # print help
                    printer.help_banner()
                elif choice == 'about':
                    printer.about()  # print about
                elif choice == '':  # Just Pass :)
                    pass
                elif choice == 'set':
                    self.noob_conf()
                elif choice == 'extract':
                    print("Not Available Right Now!")
                elif choice == 'exit':
                    # Exit From easy_mode
                    print("Exiting...")
                    time.sleep(2)
                    sys.exit(1)
                elif choice == 'clear':
                    subprocess.call('clear', shell=True)  # Clear the terminal
                elif choice == 'license':
                    printer.License()  # print the license
                elif choice == 'attacks':
                    printer.attacks()
                elif choice == "vault":
                    booker.read()  # read from the vault
                else:
                    print(writer.red("Invalid Input"))
        except KeyboardInterrupt as ki:
            """If the user enters 'Ctrl+C' exit"""
            print(writer.red('\nCtrl+C detected!', bold=True))
            time.sleep(1)
            print("Exiting...")
            time.sleep(2)

    def noob_conf(self):
        """Edit settings from easy mode."""
        try:
            print("-- Settings --")
            printer.noob_set()
            self.setC = input("[Settings]> ").__int__()
            if self.setC == 1:
                self.uid_settings()
            elif self.setC == 2:
                self.framework_settings()
            elif self.setC == 3:
                self.show_set()
            elif self.setC == 4:
                pass
            else:
                print("[{}] no such input\n".format(self.setC))
                printer.noob_set()
        except Exception as e:
            printer.unknowen_error(e)

    def show_set(self):
        """
        Show configuration file content as a python list
        """
        try:
            return settings.readOptions(self.confile)
        except Exception as e:
            printer.unknowen_error(e)
        else:
            return None

    def framework_settings(self):
        """Writing to framework settings from here"""
        try:
            print("Use Command Line Arguments\nSetings not available")
        except Exception as e:
            printer.unknowen_error(e)

    def uid_settings(self):
        """Writing to uid settings from here"""
        try:
            print("Use Command Line Arguments\nSetings not available")
        except Exception as e:
            printer.unknowen_error(e)

    def pro_conf(self):
        """Edit settings from terminal arguments mode."""
        try:
            try:
                self.index = sys.argv[2]
                if self.index == 'show':
                    print(self.show_set())
                    return
                self.value = sys.argv[3]
                self.configfile = 'core/configuration/options.conf'
                self.rdata = settings.readOptions(self.configfile)
            except Exception as e:
                print("There is 2 required arguemnts!")
                print("python Obevilion.py --set [index] [value]")
                sys.exit(1)
            if self.index == 'uid':
                if self.value == 'user' or self.value == 'root':
                    if self.index == 'uid':
                        settings.modifyLine(self.rdata, 1, self.value)
                        settings.setLine(self.configfile, self.rdata)
                    else:
                        printer.seterr()
                        sys.exit(1)
                else:
                    printer.seterr()
                    sys.exit(1)
            else:
                print("[{}] this is not an available option".format(self.index))
        except Exception as e:
            printer.unknowen_error(e)

    def main_loop(self, action=None, commands=None):
        """
        Script Main Loop
        """
        try:
            assert action in commands, "Action is not one of %s" % ', '.join(
                map(str, commands))
            try:
                # Setting up --easy_mode
                if action == '--easy_mode':
                    subprocess.call('clear', shell=True)
                    printer.main_banner()  # print the main banner
                    self.loop()  # loop in terminal
                else:
                    pass
            except Exception as e:
                pass
            if action == '--gui':
                gui.main()  # Open GUI Window
            elif action == '--cli':
                try:
                    # Setting up the args
                    self.temp = sys.argv[2]
                    self.attacks.manage_args()
                except Exception as e:
                    print(
                        'choose another argument\n-b\tfor bruteforce attack\n-d\tfor dictionary attack')
            elif action == '--help':
                printer.help_banner()  # print help banner
            elif action == '--about':
                printer.about()  # Print about
            elif action == '--about_me':
                printer.about_me()  # Print about me
            elif action == '--license':
                printer.License()  # print the license
            elif action == '--set':
                self.pro_conf()
            elif action == '--vault':
                booker.read()  # Read from the vault
            elif action == '--version':
                try:
                    # Setting up args
                    var = sys.argv[2]
                    # Run this method
                    version.vManage(var)
                except Exception as e:
                    printer.version_err()
                    sys.exit(-1)
            elif action == '--extract':
                try:
                    # Required Arguments for --extract command
                    self.option = sys.argv[2]       # File Type
                    self.path = sys.argv[3]         # file path
                    self.password = sys.argv[4]     # file password
                    self.place = sys.argv[5]        # extract place
                    try:
                        self.arc.arg_manager(
                            option=self.option, path=self.path,
                                password=self.password, place=self.place)
                    except Exception as e:
                        printer.unknowen_error(e)
                except Exception as e:
                    printer.extract_err()
                    sys.exit(-1)
            elif action == '--attacks':
                printer.attacks()
        except Exception as e:
            try:
                # If the user input invalid command
                if sys.argv[1] != commands:
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

    Methods:
    cli_bruteforce_attack_outshell: attack files in command line arguments mode
    cli_bruteforce_attack: attack files in easy_mode
    cli_dictionary_attack_outshell: dictionary attack in command arguemnts mode
    manage_args: the manager that take arguemnts to execute it
    """

    def cli_bruteforce_attack(self):
        """
        Attacking inside [the easy mode]
        """
        try:
            path = raw_input('path:')
            if path != '':  # if path not equal blank
                subprocess.call(
                    'python3 core/model.py {file}'.format(file=path), shell=True)
            else:
                print(writer.red("Try Again!"))
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
            if path == '' or path is None:  # if the user enter nothing
                print(writer.red("Try Again!"))
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
            if path == '' or path is None:  # if the user enter nothing
                print(writer.red("There Is 1 argument Messing!"))
            else:
                print(writer.yellow("Use BruteForce Attack\nTrust Me Its Better"))
        except Exception as e:
            printer.unknowen_error(e)
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
                print(writer.red("Invalid argument: {}".format(self.arg)))
        except Exception as e:
            pass


class Archives(object):
    """Managing extarcting archive files.

       Methods:
       extract_rar: extract rar files.
       extract_7z: extract 7z and zip files.."""

    def arg_manager(self, option=None, path=None, password=None, place=None):
        """
        Arguments Manager.
        if the user enters a file ending in [.zip / .7z] execute the extract_7z method
        if the user enters a file ending in [.rar] execute the extract_rar method
        else do noting
        """
        if option == '--zip' or '--7z':  # if the file type equal zip or 7z
            try:
                # Start extracting file
                self.extract_7z(path=path, password=password, place=place)
            except Exception as e:
                printer.unknowen_error(e)  # print the error
                sys.exit(-1)
        elif option == '--rar':  # if the file type equal zip or 7z
            try:
                # Start extracting file
                self.extract_rar(path=path, password=password, place=place)
            except Exception as e:
                printer.unknowen_error(e)  # print the error
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
