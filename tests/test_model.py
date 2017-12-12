# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import time
import os
import sys
import itertools
sys.path.append('../core')
from writer import Booker

# Creating instance
booker = Booker()


def rc(rf):
    # Alphabets Used in cracking
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#*+-"
    # Start Counting
    start = time.time()
    # Begin with 0 tries
    tryn = 0
    for a in range(1, len(alphabet) + 1): # for every letter in {alphabet} increase tryn with 1
        for b in itertools.product(alphabet, repeat=a):
            k = "".join(b)
            if rf[-4:] == ".rar":
                # Rar Cracing
                print("Trying:", k)
                kf = os.popen(
                    "unrar t -y -p%s %s 2>&1|grep 'All OK'" % (k, rf))
                tryn += 1
                for rkf in kf.readlines():
                    if rkf == "All OK\n":
                        # if all is 'OK', Print The Password
                        print("Found password:", repr(k))
                        print("Tried combination count:", tryn)
                        print("It took", round(time.time() - start, 3), "seconds")
                        booker.write(rf, k) # Write To The Vault
                        # Then Exit
                        print("Exiting...")
                        time.sleep(2)
                        sys.exit(1)
            elif rf[-4:] == ".zip" or rf[-3:] == ".7z":
                # Cracing zip and 7z files
                print("Trying:", k)
                kf = os.popen(
                    "7za t -p%s %s 2>&1|grep 'Everything is Ok'" % (k, rf))
                tryn += 1
                for rkf in kf.readlines():
                    if rkf == "Everything is Ok\n":
                        # if all is 'OK', Print The Password
                        print("Found password:", repr(k))
                        print("Tried combination count:", tryn)
                        print("It took", round(time.time() - start, 3), "seconds")
                        booker.write(rf, k)
                        print("Exiting...")
                        time.sleep(2)
                        sys.exit(1)
            else:
                # If the user enters invalid file type
                print("Cracking [zip / 7z / rar] only")


# Check That The File Already Exists . Then Run The File
if len(sys.argv) == 2:
    if os.path.exists(sys.argv[1]):
        rc(sys.argv[1])
    else:
        # if the file is not exist
        print("Check The File Again! , The File Not Exist.\nExiting...")
else:
    pass
