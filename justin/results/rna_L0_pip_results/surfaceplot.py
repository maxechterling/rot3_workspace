#!/usr/bin/env python


import sys
import numpy as np

gag = open(sys.argv[1])

x = []
y = []
z = []


for i in gag:
    if i.startswith("L0"):
        continue
    else:
        fields = i.rstrip("\n").split()
        x.append(np.log10(float(fields[0])))
        y.append(np.log10(float(fields[1])))
        z.append(float(fields[2]))

print "L0=", x
print "pip_binding=", y
print "gag_lattice=", z

print len(z)
"""
this is the command entered into matlab
surf(x,y,z,'FaceColor','interp','EdgeColor','none');
colormap HSV;
colorbar;
set(gca,'FontSize',20)
"""