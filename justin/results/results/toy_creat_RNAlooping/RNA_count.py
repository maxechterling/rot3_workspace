#!/usr/bin/env python

"""
takes a .gdat file and counts the number of RNA and RNApsi molecules in the polymer. Trying to see if the polymers are forming correctly

./RNA_count.py <.species>
"""

import os
import sys

print "Molecule\t" + "Gag\t" + "RNA\t" + "RNApsi\t" +"RNApsi_bound\t"
gdat = open(sys.argv[1])

line = 1
for i in gdat:
	rna = 0
	psi = 0
	psi_bound = 0
	gag = 0
	if "#" in i:
		continue
	else:
		fields = i.strip().split(".")
#		print fields
		for i in range(len(fields)):	
			if fields[i][:2] == "N(":
				rna += 1
#				if fields[i][:2] == "N(np1" need to put nu site first
			elif fields[i][:5] == "Npsi(":
				psi += 1
				if fields[i][:8] == "Npsi(nh!":
					psi_bound += 1
			elif fields[i][:3] == "GAG":
				gag += 1
	print str(line) + "\t\t" + str(gag) + "\t" + str(rna) + "\t" + str(psi) + "\t" + str(psi_bound) 
	line += 1
