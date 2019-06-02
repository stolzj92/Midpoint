import os 
import sys
import re
sam_file = open(sys.argv[1])
output_file = open("vplot.csv", "w")
#input the path of the sam file at the command line
for line in sam_file:
	if line.startswith("D"):
		split = line.split("\t")
		endposition = (split[7])
		startposition = (split[3])
		midpoint= (float(endposition)+ float(startposition))/2
		print(str(midpoint) + ",")
		