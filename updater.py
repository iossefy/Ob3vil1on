# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

"""
This file is just pulling the changes from github
"""

import sys
import shutil
import subprocess

# Check if the user have git installed on his system
for which in ["git"]:
    if not shutil.which(which):
        print("ERROR: {} isn't installed.".format(which))
        print("Exiting...")
        sys.exit(-1)

subprocess.call("clear")

print("Ob3vil1on Updater!\n")
print("Choosing the wrong branch will end with error or will break Ob3vil1on version")
print("Its Case Sensitive")
print("What Branch You Are Working On [master / Beta / development]")

try:
    branch = input("Default [master] +=> ")
except KeyboardInterrupt as e: # Detect Ctrl+c
    print("Ctrl+C detected")
    print("Exiting...")
    sys.exit(-1)

if branch != "":
    subprocess.call("git pull origin {}".format(branch), shell=True)
else:
    pass

if branch == "":
    subprocess.call("git pull origin master", shell=True)
