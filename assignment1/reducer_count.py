#!/usr/bin/python

import sys

prev_key = ()
value_total = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    key, value = line.split("\t", 1)
    value = int(value)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_key == key:
        value_total += value
    else:
        if prev_key:  # write result to stdout
            print("{0}\t{1}".format(value_total,prev_key))
            
        value_total = value
        prev_key = key

if (prev_key == key):  # Don't forget the last key/value pair
    print("{0}\t{1}".format(value_total,prev_key))
