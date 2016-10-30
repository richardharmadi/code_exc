#!/usr/bin/python

import sys
import math

prev_id=-1
name =""
total_score=0
total_value=0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    std_id, category, value = line.split("\t", 2)
    value = value.split("\t",1) 
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_id == std_id: 
	value[1] = int(value[1])
	total_score+=value[1]
	total_value+=1	
    else:
	if name:  # write result to stdout
	   print("{0}\t{1}\t{2}".format(name,total_score,total_value))          
        name=value
	total_score=0
	total_value=0
	prev_id=std_id

if (prev_id == std_id):  # Don't forget the last key/value pair
    print("{0}\t{1}\t{2}".format(name,total_score,total_value)) 
