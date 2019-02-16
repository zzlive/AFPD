# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:28:00 2018

@author: Zigan Wang
"""

import os
import pandas as pd
import numpy as np

def myFunction(a = 5, b = 4):
    if a < 10:
        print(b,a)
    c = a*b*b
    return c

def square(a = 5):
    c = a*a
    return c

def area(pi = 3.14, r = 2):
    c = pi * r * r
    return c
    