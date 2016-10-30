#!/usr/bin/python

import sys
import math

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    name, value, length = line.split("\t")
    length=float(length)
    value=float(value) 
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if (length >= 3): 
	print("{0}\t{1}".format(name,float(value/length)))	
