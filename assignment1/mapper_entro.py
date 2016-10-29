#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    value,key = line.split('\t')
    key = key.split(" ")
    print("{0} {1} {2}".format(value,key[0],key[1]))  # write the results to standard output

