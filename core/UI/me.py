# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

from tkinter import *
import os
import sys


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("About The Programmer")
        self.showTxT()

    def showTxT(self):
        # I dont know what to name the variables so forgive me
        self.title = Label(
            self.master, text="My Name Is Youssef Hesham (BL4CKvGHOST)", height=2, width=80)
        self.TxT = Label(
            self.master, text='I\'m Machine Learning Specialist.')
        self.decr = Label(
            self.master, text="Main Language Is Python")
        self.end = Label(
            self.master, text="twitter: https://www.twitter.com/BL4CKvGHOST")
        self.boom = Label(self.master, text="Website: https://www.bl4ckvghost.github.io")

        # Packing the variables
        self.title.pack()
        self.TxT.pack()
        self.decr.pack()
        self.end.pack()
        self.boom.pack()


def main():
    root = Tk()
    root.geometry('500x120')
    app = Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
