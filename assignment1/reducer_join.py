#!/usr/bin/python

import sys
import math

prev_id=-1
name =""
coursemark = []

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    std_id, category, value = line.split("\t", 2) 
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_id == std_id: 
	coursemark.append(value.replace("\t",","))	
    else:
	if name:  # write result to stdout
	   print("{0}-->{1}".format(name,coursemark))          
        name=value
	coursemark=[]
	prev_id=std_id

if (prev_id == std_id):  # Don't forget the last key/value pair
    print("{0}-->{1}".format(name,coursemark))

    
