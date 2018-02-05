#!/usr/bin/env python

"""
use an automate function to loop through a tuple list and use
os.system to put the text below into the command line
./pip_binding_number.py <.bngl> <param1> <param1_value> <param2> 
<param2_value>
"""


import sys
import os

bngl = open(sys.argv[1])



param1 = sys.argv[2]
param1_value = sys.argv[3]
param2 = sys.argv[4]
param2_value = sys.argv[5]

file = open("L0"+"_"+str(param1_value)+"_"+str(param2)+"_"+
    str(param2_value)+"_toymodel.bngl","w")


for i in bngl:
    if i.startswith("\t"+str(param1)):
        fields = i.split()
        fields[1]= str(param1_value)
        file.write( "\t" + str(fields[0]) + " " + str(fields[1]))
    elif i.startswith("\t"+str(param2)):
        fields = i.split()
        fields[1] = str(param2_value)
        file.write( "\t" + str(fields[0]) + " " + str(fields[1]))
    else:
        file.write(i)


