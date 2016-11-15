#!/usr/bin/python

import sys
maxcount = 0
for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    count,userId,answers = line.split(";")
    count=int(count) 
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted, the first line is already have the maximum accepted answers
    if(count>=maxcount):
    	print("{0} -> {1}, {2}".format(userId,count,answers))
	maxcount=count
