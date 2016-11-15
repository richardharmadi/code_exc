#!/usr/bin/python

import sys,os,re

filename = os.environ["mapreduce_map_input_file"].split('/')[-1]

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    tokens = re.findall(r"[\w']+",line)
    for token in tokens:
	print("{0};{1};{2}".format(filename,token,1))
