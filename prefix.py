"""
ID: wrwwctb1
LANG: PYTHON3
TASK: prefix
2.3.1

key idea
dp
"""

import os, sys, re, itertools, functools, heapq
from collections import Counter, deque
from copy import copy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
             sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan

print = functools.partial(print, flush=True)
input = lambda: fin.readline().strip()

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'prefix'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')








primitives = []
while True:
    line = input()
    if line == '.':
        break
    primitives.extend(line.split())

primitives = set(primitives)

string = []
while True:
    line = input()
    if line == '':
        break
    string.append(line)
string = ''.join(string)

ln = len(string)

# initialize
can = [0] * ln
for primitive in primitives:
    lnp = len(primitive)
    if string[:lnp] == primitive:
        can[lnp-1] = 1

# crawl
for i in range(1, ln):
    if can[i] == 0:
        for primitive in primitives:
            lnp = len(primitive)
            prev = i - lnp
            if prev >= 0 and can[prev] == 1 and string[prev+1:i+1] == primitive:
                can[i] = 1
                break

# find last 1
idx = ln-1
while idx >= 0:
    if can[idx] == 1:
        break
    idx -= 1
printwrite(idx+1)








fin.close()
fout.close()
del print, input

