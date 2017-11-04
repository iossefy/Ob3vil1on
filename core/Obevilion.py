# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

# Import The Needed Lib
import time
import os
import sys
import shutil
import itertools
import Banner

def get_name():
    '''
    in this method we are getting the name of the current file
    if the user running the main file out the core folder it must
    be running from a .pyc file
    i have changed the name of the .pyc file to .py file temporary only
    it will be changed soon, this is just a small bug
    '''
    name = os.path.basename(__file__)
    if "pyc" not in name:
        return name
    else:
        return "Obevilion.py"
    return None

def rc(rf):
    # The Keywords that will be used in cracking
    alphabet="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@<>"
    start=time.time()
    tryn=0
    '''
    in this function the 'alphabet' will repeat itself
    until the script find the password
    this Operation called bruteforce attack
    '''
    for a in range(1,len(alphabet)+1):
        for b in itertools.product(alphabet,repeat=a):
            k="".join(b)
            # If the user input a rar file,
            # Execute this.
            if rf[-4:]==".rar":
                print("Trying:",k)
                # Checking The Valid Password.
                kf=os.popen("unrar t -y -p%s %s 2>&1|grep 'All OK'"%(k,rf))
                tryn+=1
                for rkf in kf.readlines():
                    if rkf=="All OK\n": # Checking if all is ok.
                        print("Password Cracked!:",repr(k))
                        print("Tried combination count:",tryn)
                        print("It took",round(time.time()-start,3),"seconds")
                        print("Exiting...")
                        time.sleep(2)
                        sys.exit(1)
                # If the user input a zip or 7z file
                # Execute this.
            elif rf[-4:]==".zip" or rf[-3:]==".7z":
                print("Trying:",k)
                kf=os.popen("7za t -p%s %s 2>&1|grep 'Everything is Ok'"%(k,rf))
                tryn+=1
                for rkf in kf.readlines():
                    if rkf=="Everything is Ok\n":
                        print("Password Cracked:",repr(k))
                        print("Tried combination count:",tryn)
                        print("It took",round(time.time()-start,3),"seconds")
                        print("Exiting...")
                        time.sleep(2)
                        sys.exit(1)
                    else:
                        # If the user inputs a wrong type of archive
                        print("We Are Cracking (rar , zip , 7z) only")
                        print('Exiting...')
                        time.sleep(2)
                        sys.exit(1)

def script(path=None, limit=3):
    '''
    This is the main script that all the program About.
    This will take the parameter path and try to crack it
    with the bruteforce attack by looping arround the alphabet
    and symboles until the script get the valid password
    Arg path: the path of the archive to crack
    Arg limit: The script arguments limit
    '''
    # checking if the user's operating system is compatible with Obevilion
    if os.name!="posix":
        print("ERROR:",name,"isn't compatible with your system yet!")
        print("Exiting...")
        time.sleep(2)
        sys.exit(-1)
        # checking if the user Have Unrar And Unzip
        for req in ["unrar","p7zip"]:
            if not shutil.req(req):
                print("ERROR: %s isn't installed." % req)
                print("Exiting...")
                time.sleep(2)
                sys.exit(-1)

    # Check That The File Already Exists . Then Run The File
        if len(sys.argv)==limit:
            if os.path.exists(path):
                rc(path)
            else:
                print("Check The File Again!, The File Not Exist.")
                print("Exiting...")
                time.sleep(2)
                sys.exit(1)
