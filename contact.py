"""
ID: wrwwctb1
LANG: PYTHON3
TASK: contact
3.1.5

key idea
count the number of every bit pattern seen
use an array to keep the counts
the index is bit pattern with a leading 1 prepended, eg to separate 01 and 001
"""

import os, sys, re, time
from collections import Counter, deque, defaultdict
from queue import Queue
from copy import copy, deepcopy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key, partial as functools_partial
from heapq import heappush, heappop, nlargest, nsmallest
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
         pi, sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan
# sys.setrecursionlimit(5782)
# python -m cProfile -s time ha.py

print = functools_partial(print, flush=True)
input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'contact'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')
ttt = time.time()










A, B, N = map(int, input().split())

string = []
while True:
    line = input()
    if line == '':
        break
    string.append(line)
string = ''.join(string)


Ncounts = 10000
counts = [0] * Ncounts

Nstring = len(string)
for i in range(Nstring):
    for l in range(A, B + 1):
        if i + l > Nstring:
            break
        sub = string[i:i+l]
        idx = int(sub, 2)
        idx ^= 1 << l
        counts[idx] += 1

counts = list(zip(counts, range(Ncounts)))

counts.sort(key=lambda cnt_idx: (-cnt_idx[0], cnt_idx[1]))


# collect results
out = defaultdict(list)
countsIdx = 0
while True:
    currCnt, currBits = counts[countsIdx]
    if currCnt == 0:
        break
    if (len(out) > N or (len(out) == N and currCnt not in out)):
        break
    out[currCnt].append(currBits)
    countsIdx += 1

# output
for key in sorted(out.keys(), reverse=True):
    printwrite(key)
    vals = out[key]
    outVals = []
    for val in vals:
        outVals.append(bin(val)[3:])
    i = 0
    while i < len(outVals):
        if i + 6 < len(outVals):
            printwrite(' '.join(['%s'] * 6) % tuple(outVals[i:i+6]))
        else:
            r = len(outVals) - i
            printwrite(' '.join(['%s'] * r) % tuple(outVals[i:i+r]))
        i += 6












fin.close()
fout.close()
del print, input
print(time.time() - ttt)
