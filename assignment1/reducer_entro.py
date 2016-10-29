#!/usr/bin/python

import sys
import math

prev_key = ""
value_total = 0
log_key = 0.0
ent = 0.0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    value, key = line.split(" ", 1)
    value = int(value) 
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_key == key:
        value_total += value
        log_key += value * math.log(value,2) # log base 2
    else:
	if prev_key:  # write result to stdout
	   ent = (-log_key/value_total)+math.log(value_total,2)
	   print ("{0}\t{1}".format(prev_key,ent))	
           
        value_total = value
        prev_key = key
	log_key = value * math.log(value,2) # log base 2
 
if (prev_key == key):  # Don't forget the last key/value pair
    ent = (-log_key/value_total)+math.log(value_total,2)
    print("{0}\t{1}".format(prev_key,ent))
