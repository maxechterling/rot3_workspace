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

# Nt is the max number of RNAs in the system
# Nh0 is the max number of PSI RNAs in the system
# RNA creation rate was at Khigh anyways
Nt= [2000,4000,8000,16000,32000]
Nh0= [200,400,800,1600,3200]

combined = []

for i in Nt:
    for p in Nh0:
        combined.append((i,p))

print combined
print combined[0][0]

count = 0 
for i in range(len(combined)):
    os.system("./Nt_Nh0_cooperativity.py " + "toy_creat_RNAlooping_PSI_cooperativity.bngl " + 
        "Nt " + str(combined[i][0]) + " " + "Nh0 " + str(combined[i][1]))