# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

# framework = {'mode':True, 'easy_mode':False}
# user = {'uid':'root', 'guid':'root'}

"""
Reading and writing to the configuration file.
configuration file is located in {$PROJECT}/core/configuration/options.conf.

What is this class do?
this is the configuration manager.
first: read the data from options.conf
then modify it in modify method.
then write it to options.conf

Methods:
readOptions: return contents of the conf file
getLine: get specific line
modifyLine: Modify the given list.
setLine: write to givin file
"""


def readOptions(config):
    """
    Reading all the lines in {$config}
    file as a list then return it

    config: target file
    """
    with open(config) as config:
        line = config.readlines()
        return line


def getLine(data, index):
    """
    Getting specific line.

    data: returned data from readOptions() method
    index: target index to change
    """
    return data[index].replace('\n', '')


def modifyLine(txt, cell, value):
    """
    modifying specific cell in the givin list.

    txt: returned data from readOptions() method
    cell: target cell to change
    value: text to replace the old with
    """
    txt[cell] = '{}\n'.format(value)


def setLine(conf, data):
    """
    Writing to the file.

    conf: target file
    data: modified data
    """
    with open(conf, 'w') as confile:
        confile.writelines(data)
