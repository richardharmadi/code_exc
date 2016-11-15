#!/usr/bin/python

import sys
maxvalue=0
for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    value,userId,questions = line.split(";")
    value=int(value)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted, the first line is already the user that answered the most questions
    if (value>=maxvalue):
	#print("{0},{1}".format(value,userId))
    	print("{0} -> {1}".format(userId,questions))
	maxvalue=value
