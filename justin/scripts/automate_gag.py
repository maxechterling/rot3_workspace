#!/usr/bin/env python

"""
creates a new file for every permutation of the two lists you give it.
./<.py> script uses the file name to direct the change in the bngl file

"""
import sys
import itertools
import os
import matplotlib.pyplot as plt
import numpy as np
import math


L_0= [10,50,100,500,1000,5000,10000,50000,100000,500000]
pip= [100,500,1000,5000,10000,50000,100000,500000,1000000,5000000]

combined = []

for i in L_0:
    for p in pip:
        combined.append((i,p))

print combined
print combined[0][0]

count = 0 
for i in range(len(combined)):
    os.system("./pip_binding_number.py " + "toy_creat_RNAlooping_gagprod_10000.bngl " + 
        "L_0 " + str(combined[i][0]) + " " + "pip " + str(combined[i][1]))