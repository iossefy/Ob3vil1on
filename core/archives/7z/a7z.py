# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

from subprocess import call
from sys import exit
from time import sleep

def extr_arc(path=None, password=None, dist=None):
    if path==None:
        print("Path argument not exists!")
        sleep(1)
        exit(0)
    else:
        if password!=None:
            if dist==None:
                print("distination Missing!")
                exit(0)
            call('7za t -p{pwd} {filename} {distination}'.format(pwd=password, filename=path, distination=dist), shell=True)
        elif password==None:
            if dist==None:
                print("distination Missing!")
                exit(0)
            call('7z x {} {}'.format(path, dist))
