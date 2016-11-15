#!/usr/bin/python

import sys
n = 0
for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    viewCount,postId = line.split(";")
    n+=1
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if n<=10:
    	print("{0} {1}".format(viewCount,postId))
