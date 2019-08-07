"""
ID: wrwwctb1
LANG: PYTHON3
TASK: shopping
3.3.3

key idea

similar to knapsack
k_abcde: min price when quantities of item 0/1/2/3/4 are a/b/c/d/e
(ai, bi, ci, di, ei), pi: # of items, price of offer i

k_00000 = 0
k_abcde = min k_(a-ai)(b-bi)(c-ci)(d-di)(e-ei) + pi
           *
           condition: a>=ai, b>=bi, c>=ci, d>=di, e>=di



regular knapsack does not need all W be filled

here abcde is guaranteed to be filled because each item has a corresponding
offer for quantity 1. when going through k, abcde is filled at every step



dijkstra is ok but needs c++ to pass
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

filename = 'shopping'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')










class Offer:
    def __init__(self, line):
        #self.numtypes = line[0] # 1-5
        types = line[1:-1:2]
        cnts = line[2:-1:2]
        self.counter = Counter()
        for i in range(line[0]):
            self.counter[types[i]] = cnts[i] # 1-999, 1-5
        self.price = line[-1] # 1-9999
        self.content = None

    def __repr__(self):
        out = '\n%d ' % self.price + str(self.counter)
        return out


numoffers = int(input()) # 0-99
offers = []

for i in range(numoffers):
    line = list(map(int, input().split()))
    offers.append(Offer(line))

numtypesneeded = int(input()) # 0-5

need = Counter()

for i in range(numtypesneeded):
    c, k, p = map(int, input().split())
    offers.append(Offer([1, c, 1, p])) # 1-999, 1-999
    need[c] += k # 1-5


# simplify state from counter to list. remove pointless types
if len(need) > 0:
    typesneeded, needtuple = zip(*sorted(need.items()))
else:
    typesneeded = needtuple = ()

for offer in offers:
    content = []
    for typ in typesneeded:
        content.append(offer.counter[typ])
    offer.content = content




# maxnumtypesneeded = 6
need5d = needtuple + (0,) * (5-len(needtuple))
for offer in offers:
    content5d = offer.content + [0] * (5-len(needtuple))
    offer.content5d = content5d

k = [[[[[inf for a in range(need5d[4]+1)] for b in range(need5d[3]+1)]
             for c in range(need5d[2]+1)] for d in range(need5d[1]+1)]
             for e in range(need5d[0]+1)] # 5d
k[0][0][0][0][0] = 0

for a in range(need5d[0]+1):
    for b in range(need5d[1]+1):
        for c in range(need5d[2]+1):
            for d in range(need5d[3]+1):
                for e in range(need5d[4]+1):
                    if a == b == c == d == e == 0:
                        continue
                    cand = inf
                    for offer in offers:
                        ai, bi, ci, di, ei = offer.content5d

                        if a >= ai and b >= bi and c >= ci and \
                           d >= di and e >= ei:
                            candi = k[a-ai][b-bi][c-ci][d-di][e-ei] + \
                                    offer.price
                            if candi < cand:
                                cand = candi
                    k[a][b][c][d][e] = cand

printwrite(k[-1][-1][-1][-1][-1])









fin.close()
fout.close()
del print, input

