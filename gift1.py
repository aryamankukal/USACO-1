"""
ID: wrwwctb1
LANG: PYTHON3
TASK: gift1
1.2.5
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

filename = 'gift1'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')





NP = int(input())
name2id = {}
id2name = []
for np in range(NP):
    name = input()
    name2id[name] = np
    id2name.append(name)

balance = [0] * NP

for np in range(NP):
    personId = name2id[input()]
    get, giveNum = map(int, input().split())
    if giveNum != 0:
        give, keep = divmod(get, giveNum)
        balance[personId] += -get + keep
        for givenum in range(giveNum):
            otherId = name2id[input()]
            balance[otherId] += give
    else:
        balance[personId] += get

for np in range(NP):
    printwrite('%s %d' % (id2name[np], balance[np]))



fin.close()
fout.close()
del print, input

