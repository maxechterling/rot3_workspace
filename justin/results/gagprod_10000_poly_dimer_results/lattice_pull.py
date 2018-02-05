#!/usr/bin/env python


"""
use the bash command to call this script. Make sure to change based on
observables and filenames
"""
import sys
import os

gdat = open(sys.argv[1])

gdat_name = sys.argv[1]


last = gdat.readlines()[-1]
line = last.split()

fields = gdat_name.split("_")
print fields[3] + "\t" + fields[5] + "\t" + str(float(line[9][:6])*10**float(line[9][-1]))


#gdat.seek(-2)








