#!/usr/bin/env python

import sys
import os

gdat = open(sys.argv[1])

gdat_name = sys.argv[1]


last = gdat.readlines()[-1]
line = last.split()

fields = gdat_name.split("_")
print fields[1] + "\t" + fields[3] + "\t" + str(float(line[6][:6])*10**float(line[6][-1]))


#gdat.seek(-2)








