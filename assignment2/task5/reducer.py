#!/usr/bin/python

import sys
import random
line_number = 0

for line in sys.stdin:
    if random.randint(0, line_number) == 0:
        resevoir = line.strip()
    line_number += 1
print(resevoir)
