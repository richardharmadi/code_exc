#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    char_count = len(line)
    tokens = line.split()
    longest_token = 0

    for token in tokens:
	if (len(token)>longest_token):	
        	longest_token = len(token)
    print ("{0}\t{1}\t{2}".format(line,char_count,longest_token)) # write the results to standard output
