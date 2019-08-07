"""
ID: wrwwctb1
LANG: PYTHON3
TASK: job
4.2.4

key idea
not network flow, which gives steady state response

            A delay               B delay
        *                   *******************
        **                          ***********
        ****                             ******
jobs    *******                           *****
        ***********                         ***
        ********************                  *
"""

import os, sys, re
from collections import Counter, deque, defaultdict
from copy import copy
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

filename = 'job'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')














def getFinishTimes(N, delays):
    # N M
    # can be N lg M if sorted set were available
    delays0 = copy(delays)
    t = []
    for n in range(N):
        earliestFinish_t = min(delays)
        earliestFinish_i = delays.index(earliestFinish_t)
        t.append(earliestFinish_t)
        delays[earliestFinish_i] += delays0[earliestFinish_i]
    return t


N, MA, MB= map(int, input().split())
line = []
while True:
    temp = input()
    if temp == '':
        break
    line += list(map(int, temp.split()))

delaysA = line[:MA]
delaysB = line[MA:]

tA = getFinishTimes(N, delaysA)
tB = getFinishTimes(N, delaysB)[::-1]

t_finish = [tA[n] + tB[n] for n in range(N)]

printwrite('%d %d' % (max(tA), max(t_finish)))
















fin.close()
fout.close()
del print, input

