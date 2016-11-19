#!/usr/bin/python

import sys

prev_userId = ""
value_total = 0
questions=[]
for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    userId,questionId,value = line.split(";")
    value = int(value)
    #questionId = int(questionId)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_userId == userId:
        value_total += value
	questions.append(questionId)
    else:
        if prev_userId:  # write result to stdout
            print("{0};{1};{2}".format(prev_userId,', '.join(questions),value_total))
            
        value_total = value
        prev_userId = userId
	questions = [questionId]

if (prev_userId == userId):  # Don't forget the last key/value pair
    print("{0};{1};{2}".format(prev_userId,', '.join(questions),value_total))
