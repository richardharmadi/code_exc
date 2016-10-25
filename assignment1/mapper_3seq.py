#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    tokens = line.split()

    for i in range(len(tokens)-3+1): # number of words in line - n-word sequence + 1
	trio = tuple(tokens[i:i+3])
    	print ("{0}\t{1}".format(trio,1)) # write the results to standard output
