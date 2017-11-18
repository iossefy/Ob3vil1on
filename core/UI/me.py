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
        self.TxT = Label(
            self.master, text='IAM A PROGRAMMER!', pady=60, padx=60)
        self.decr = Label(self.master, text="Go Back Fool!", pady=70, padx=70)
        self.TxT.pack()
        self.decr.pack()


def main():
    root = Tk()
    root.geometry('500x300')
    app = Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
