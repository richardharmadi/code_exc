#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    filename,word,value = line.split(';')
    value = int(value)
    pair = (filename,value)
    print("{0};{1};{2}".format(word,pair,1))
