#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    answerId,userId = line.split('\t')
    print("{0};{1};{2}".format(userId,answerId,1))
