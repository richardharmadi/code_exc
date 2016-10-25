#!/usr/bin/python

import sys

longest_line = 0
longest_word = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip("\n")         # Remove trailing characters
    line, len_line, len_word = line.split("\t")
    len_line = int(len_line)
    len_word = int(len_word)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if len_line > longest_line:
        longest_line = len_line
    
    if len_word > longest_word:
        longest_word = len_word   

print("{0}\t{1}".format(longest_word, longest_line))
