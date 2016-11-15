#!/usr/bin/python

import sys
prevId=-1
value_total=0
answers=[]
for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    userId,answerId,value = line.split(";")
    value = int(value)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if (prevId == userId):
	value_total+=value
	answers.append(answerId)
    else:
	if (prevId>=0):
	   print("{0};{1};{2}".format(prevId,value_total,', '.join(answers)))
	prevId = userId
	value_total=value
	answers=[answerId]
