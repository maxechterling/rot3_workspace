#!/usr/bin/env python


import sys
import numpy as np

gag = open(sys.argv[1])

x = []
y = []
z = []


for i in gag:
    if i.startswith("poly"):
        continue
    else:
        fields = i.rstrip("\n").split()
        print fields
        x.append(float(fields[0]))
        y.append(float(fields[1]))
        z.append(float(fields[2]))

print "N=", x
print "Psi=", y
print "lattice=", z

print len(z)
"""
this is the command entered into matlab
surf(x,y,z,'FaceColor','interp','EdgeColor','none');
colormap HSV;
colorbar;
set(gca,'FontSize',20)
"""