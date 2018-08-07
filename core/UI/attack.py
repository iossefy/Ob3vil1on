# -*- coding: utf-8 -*-

# @author MaliciouSSymbol
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

import time
import os
import sys
import itertools
sys.path.append("{cur}/core".format(cur=os.getcwd()))
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
                        try:
                            output.append(
                                "Found password {pwd}\nTried combination count {num}\nIt toook {time} seconds\nTerminating...".format(
                                    pwd=str(k), num=str(tryn), time=round(time.time() - start, 3)))
                        except Exception as e:
                            output.append(str(e))
                        booker.write(rf, k)
            elif rf[-4:] == ".zip" or rf[-3:] == ".7z":
                output.append("Trying: {}".format(k))
                kf = os.popen(
                    "7za t -p%s %s 2>&1|grep 'Everything is Ok'" % (k, rf))
                tryn += 1
                for rkf in kf.readlines():
                    if rkf == "Everything is Ok\n":
                        output.append(str(k))
                        try:
                            output.append(
                                "Found password {pwd}\nTried combination count {num}\nIt toook {time} seconds\nTerminating...".format(
                                    pwd=str(k), num=str(tryn), time=round(time.time() - start, 3)))
                            booker.write(rf, k)
                            return
                        except Exception as e:
                            output.append(str(e))
            else:
                output.append("Cracking [zip / 7z / rar] only")


# Check That The File Already Exists . Then Run The File
# if os.path.exists(sys.argv[1]):
#     rc(sys.argv[1], sys.argv[2])
# else:
#     output.append("Check The File Again! , The File Not Exist.\nExiting...")
