# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import sys
<<<<<<< HEAD
import subprocess
from core import Banner, Obevilion, Check, Control
from core.UI import gui

check_req  = Check.Check_req()
printer    = Banner.Printer()
looprocess = Control.LoopControl()
action     = ''
commands   = ['--gui', '--cli', '--help', '--about', '--easy_mode', '--about_me', '--license']

try:
    action = sys.argv[1]
except Exception as e:
    printer.main_banner()

def loop_action(action): # Using the easy loop system
    if action == '--easy_mode':
        printer.main_banner
        looprocess.loop()
    else:
        pass

def main():

    check_req.check_os() # Checking the required operation system
    check_req.check_py_version() # Check valid python version
#    check_req.check_softwares() # Checking if the user have the required softwares
    looprocess.main_loop(action=action, commands=commands) # Run

if __name__ == '__main__':
    main()
=======
import shutil
import itertools

name=os.path.basename(__file__)

#checking if the user's operating system is compatible with Obevilion
if os.name!="posix":
    print("ERROR:",name,"isn't compatible with your system yet!")
    sys.exit(-1)
    #checking if the user Have Unrar And Unzip
    for which in ["unrar","p7zip"]:
        if not shutil.which(which):
            print("ERROR:",which,"isn't installed.\nExiting...")
            sys.exit(-1)

#defining the functions
def rc(rf):
    alphabet="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890@#<>"
    start=time.time()
    tryn=0
    for a in range(1,len(alphabet)+1):
        for b in itertools.product(alphabet,repeat=a):
            k="".join(b)
            if rf[-4:]==".rar":
                print("Trying:",k)
                kf=os.popen("unrar t -y -p%s %s 2>&1|grep 'All OK'"%(k,rf))
                tryn+=1
                for rkf in kf.readlines():
                    if rkf=="All OK\n":
                        print("Password Cracked!:",repr(k))
                        print("Tried combination count:",tryn)
                        print("It took",round(time.time()-start,3),"seconds")
                        print("Exiting...")
                        time.sleep(2)
                        sys.exit(1)
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
                                print("We Are Cracking (rar , zip , 7z) only  \nExiting...")

# Check That The File Already Exists . Then Run The File
    if len(sys.argv)==2:
        if os.path.exists(sys.argv[1]):
            rc(sys.argv[1])
        else:
            print("Check The File Again! , The File Not Exist.\nExiting...")
    else:
        print('''

████▄ ███   ▄███▄      ▄   ▄█ █    ▄█ ████▄    ▄
█   █ █  █  █▀   ▀      █  ██ █    ██ █   █     █
█   █ █ ▀ ▄ ██▄▄   █     █ ██ █    ██ █   █ ██   █
▀████ █  ▄▀ █▄   ▄▀ █    █ ▐█ ███▄ ▐█ ▀████ █ █  █
      ███   ▀███▀    █  █   ▐     ▀ ▐       █  █ █
                      █▐                    █   ██
                      ▐
                           NO ONE WILL GIVE YOU FREEDOM
                           YOU TAKE IT!
''')
 print("OBEVILION")
 print("Updates: now officialy obevilion is the strongest Cracking Script")
 print("Coded By BL4CKvGHOST")
 print("GitHub: https://github.com/BL4CKvGHOST")
 print("Twitter: https://twitter.com/BL4CKvGHOST")
 print("Usage:",name,"[path to rar file]")
 print("Example:","Python3 ",name,"example.zip")
>>>>>>> master
