#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    tokens = line.split()

    for i in range(len(tokens)-3+1): # number of words in line - n-word sequence + 1
	print ("{0} {1} {2}\t{3}".format(tokens[i],tokens[i+1],tokens[i+2],1)) # write the results to standard output
