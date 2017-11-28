# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

from subprocess import call
from time import sleep
from sys import exit

def extr_arc(path=None, password=None, dist=None):
    if path==None:
        print("Path argument not exists!")
        sleep(1)
        exit(0)
    else:
        if password!=None:
            if dist==None:
                print("distination Missing!")
            subprocess.call('unrar x -p{pwd} {name} {distination}'.format(pwd=password, name=path, distination=dist), shell=True)
        elif password==None:
            if dist==None:
                print("distination Missing!")
            subprocess.call('unrar x {name} {distination}'.format(name=path, distination=dist))
