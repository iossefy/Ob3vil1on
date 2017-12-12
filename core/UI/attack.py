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
sys.path.append("../")
from writer import Booker

booker = Booker()


def rc(rf, output):
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#*+-"
    start = time.time()
    tryn = 0
    for a in range(1, len(alphabet) + 1):
        for b in itertools.product(alphabet, repeat=a):
            k = "".join(b)
            if rf[-4:] == ".rar":
                output.append("Trying:", k)
                kf = os.popen(
                    "unrar t -y -p%s %s 2>&1|grep 'All OK'" % (k, rf))
                tryn += 1
                for rkf in kf.readlines():
                    if rkf == "All OK\n":
                        output.append("Found password: {}".format(str(k)))
                        output.append(
                            "Tried combination count: {}".format(tryn))
                        output.append("It took {} seconds".format(
                            round(time.time() - start, 3)))
                        booker.write(rf, k)
                        output.append("Exiting...")
            elif rf[-4:] == ".zip" or rf[-3:] == ".7z":
                output.append("Trying: {}".format(k))
                kf = os.popen(
                    "7za t -p%s %s 2>&1|grep 'Everything is Ok'" % (k, rf))
                tryn += 1
                for rkf in kf.readlines():
                    if rkf == "Everything is Ok\n":
                        output.append("Found password:", str(k))
                        output.append("Tried combination count:", tryn)
                        output.append("It took {} seconds".format(
                            round(time.time() - start, 3)))
                        booker.write(rf, k)
                        output.append("Exiting...")
            else:
                output.append("Cracking [zip / 7z / rar] only")


# Check That The File Already Exists . Then Run The File
# if os.path.exists(sys.argv[1]):
#     rc(sys.argv[1], sys.argv[2])
# else:
#     output.append("Check The File Again! , The File Not Exist.\nExiting...")
