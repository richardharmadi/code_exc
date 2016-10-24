#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    line = line.upper()
    print("{0}\t{1}".format(line,1))  # write the results to standard output

