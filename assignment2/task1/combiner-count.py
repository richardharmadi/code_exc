#!/usr/bin/python

import sys

prev_key = ""
value_total = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    filename,keyvalue = line.split(";",2)
    key,value = keyvalue.split()
    value = int(value)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_key == key:
        value_total += value
    else:
        if prev_key:  # write result to stdout
            print("{0};{1}\t{2}".format(filename,prev_key,value_total))
        value_total = value
        prev_key = key

if (prev_key == key):  # Don't forget the last key/value pair
    print("{0};{1}\t{2}".format(filename,prev_key,value_total))
