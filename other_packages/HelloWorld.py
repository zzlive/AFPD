# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 16:46:24 2018

@author: Zigan Wang
version: 1.1

This whole code is to explain the basic programming
and the writing of hello world codes for the MFIN
students.
"""

import os

path = 'C:\\Users\\Zigan Wang'

#the following code generates 100 hello word txt files
for i in range(100):
    file_name = 'HelloWorld_' + str(i+1) + '.txt'
    f = open(path + os.sep + file_name,'w')
    content = 'Hello World for the ' + str(i+1) + ' time!'
    f.write(content)
    f.close()
    
if type(x) == 'int':
    print('computation could be correct')

#delete 100 hello word txt files
for i in range(100):
    file_name = 'HelloWorld_' + str(i+1) + '.txt'
    os.remove(path + os.sep + file_name)