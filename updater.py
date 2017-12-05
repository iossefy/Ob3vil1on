# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
This file is just pulling the changes from github
"""

import sys
import shutil
import subprocess

# Check if the user have git installed on his system
for which in ["git"]:
    if not shutil.which(which):
        print("ERROR: %s isn't installed." % which)
        print("Exiting...")
        sys.exit(-1)

subprocess.call("clear")

print("Ob3vil1on Updater!\n")
print("Choosing the wrong branch will end with error or will break Ob3vil1on version")
print("What Branch You Are Working On [master / Beta / development]")
branch = input("Default [master] +=> ")

if branch!="":
    subprocess.call("git pull origin {}".format(branch), shell=True)
else:
    pass

if branch=="":
    subprocess.call("git pull origin master", shell=True)
