"""
ID: wrwwctb1
LANG: PYTHON3
TASK: ariprog
1.5.2

conceptually, it's faster to look at each arithmetic progression until its end,
then record the starting points that give enough length, and then never revisit

but in practice, it's faster to loop thru all differences and try to use each
bisquare as the head of an arithmetic progression, with some pruning

this could be because bisquares' distribution being irregular
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

filename = 'ariprog'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









# < 1s with numba
# compilation makes a huge difference
# usaco doens't have numba

#from numba import jit
#@jit
def wrapper(maxdiff, bsqls, N, maxbsq, bsqtf):
    out = [] # overall faster than printing in the loop

    for b in range(1, maxdiff+1):

        for a in bsqls:

            last = a + (N-1)*b
            if last > maxbsq:
                break
            if not bsqtf[last]:
                continue
            if not bsqtf[a + b]:
            #if a + b not in bsqst:
                continue

            founddepth = 1
            curr = a
            while founddepth < N:
                curr += b
                if not bsqtf[curr]:
                #if curr not in st:
                    break
                else:
                    founddepth += 1

            if N == founddepth:
                out.append((a, b))
    #        else: # 1 < founddepth < N
    #            # record visited along the way. neither tf or st helps
    return out

#import time
#tt = time.time()

N = int(input())
M = int(input())

maxbsq = M * M * 2
bsqst = set()
bsqtf = [False] * (maxbsq + 1) # marginally faster than st
for p in range(M+1):
    for q in range(p, M+1):
        bsq = p*p + q*q
        bsqst.add(bsq)
        bsqtf[bsq] = True
bsqls = sorted(bsqst)

maxdiff = maxbsq // (N-1)

out = wrapper(maxdiff, bsqls, N, maxbsq, bsqtf)

if len(out) == 0:
    printwrite('NONE')
else:
    for a, b in out:
        printwrite('%d %d' % (a, b))

#print(time.time()-tt)








fin.close()
fout.close()
del print, input

