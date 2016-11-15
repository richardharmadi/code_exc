#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    userId,count,answers = line.split(';')
    print("{0};{1};{2}".format(count,userId,answers))
