#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    userId,questions,value = line.split(';')
    print("{0};{1};{2}".format(value,userId,questions))
