#!/usr/bin/python

import sys
import random

k = 10 # number of lines that we want to sample
resevoir = []

for i in range(k): 
    resevoir.append(sys.stdin.readline())
line_number=k

for line in sys.stdin:
    if random.randint(0, line_number) == 0:
        resevoir = line.strip()
    line_number += 1
print(resevoir)
