#!/usr/bin/python

import sys

prev_sentence = ""
value_total = 0
sentence = ""

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    sentence, value = line.split("\t", 1)
    value = int(value)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_sentence == sentence:
        value_total += value
    else:
        if (prev_sentence) and (value_total == 1):  # write result to stdout
            print("{0}\t".format(prev_sentence))
            
        value_total = value
        prev_sentence = sentence

if (prev_sentence == sentence)and(value_total == 1):  # Don't forget the last key/value pair
    print("{0}\t".format(prev_sentence))
