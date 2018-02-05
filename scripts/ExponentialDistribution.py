#!/usr/bin/env python

"""
Usage:
    
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

# Rate of reaction = lamb
lamb = .0106
x = [ i for i in range(30) ]
y = [ lamb*2.71828 ** (-lamb*i) for i in x ]
# This will get you the random draw from the exponential distribution
y2 = [ np.random.exponential( 1./lamb ) for i in range(10000) ]
print y2

plt.figure()
plt.hist( y2, bins=50 )
plt.show()
plt.close()