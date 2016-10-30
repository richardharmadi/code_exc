#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    category, std_id,value = line.split("\t",2) 
    print("{0}\t{1}\t{2}".format(std_id,category,value))  # write the results to standard output
