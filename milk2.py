"""
ID: wrwwctb1
LANG: PYTHON3
TASK: milk2
1.3.2

key idea
sort intervals by start time, merge overlapping intervals, find longest on and longest off durations

alternative
bool array for all 1000000 seconds
check longest consecutive 1's and then 0's
but such checking is more complicated than mergeIntervals
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

filename = 'milk2'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')








def mergeintervals(intervals):
    intervals.sort(key=lambda interval: interval[0])
    out = []
    currstart, currend = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= currend:
            currend = max(currend, intervals[i][1])
        else:
            out.append([currstart, currend])
            currstart, currend = intervals[i]
    out.append([currstart, currend])
    return out



N = int(input())
times = []
for n in range(N):
    cow = list(map(int, input().split()))
    times.append(cow)

merged = mergeintervals(times)

bestmilk = merged[0][1] - merged[0][0]
bestnomilk = 0
for i in range(1, len(merged)):
    bestmilk = max(bestmilk, merged[i][1] - merged[i][0])
    bestnomilk = max(bestnomilk, merged[i][0] - merged[i-1][1])

printwrite('%d %d' % (bestmilk, bestnomilk))







fin.close()
fout.close()
del print, input

