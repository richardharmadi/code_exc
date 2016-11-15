#!/usr/bin/python

import sys

prevId=-1

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    key,value = line.split("\t") # value = user id
    answerId,postId = key.split(";") 
    if (prevId==answerId):
	if (value): 
		print("{0}\t{1}".format(prevId,value))	
    prevId=answerId
