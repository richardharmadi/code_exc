#!/usr/bin/python

import sys

prev_key = ""
value_total = 0
pairs=[]

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    key,pair,value = line.split(";")
    value = int(value)
    pair = str(pair)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_key == key:
        value_total += value
	pairs.append(pair)
    else:
        if prev_key:  # write result to stdout
           print("%s : %s : {%s}"%(prev_key,value_total,','.join(pairs)))
        value_total = value
        prev_key = key
	pairs = [pair]

if (prev_key == key):  # Don't forget the last key/value pair
    print("%s : %s : {%s}"%(prev_key,value_total,','.join(pairs)))
