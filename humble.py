"""
ID: wrwwctb1
LANG: PYTHON3
TASK: humble
3.1.4

key idea
N lg K sol
let H be the sorted sequence of humble nums
imagine each prime has a line: pH0, pH1, pH2...
Among all lines' heads, choose min to feed H


N K lg N sol
use c++ set<>
keep taking the smallest humble# stored
insert reachable humble#s
only keep required number of humble#s in the set

why c++ set<>:
    log-time min, max, insert and delete
    max and delete (unavailable to py heapq) are needed to keep the set small

usaco sol is K N N. can be optimized to K N lg N using bisect
"""

import os, sys, re
from collections import Counter, deque, defaultdict
from copy import copy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key
from functools import partial as functools_partial
from heapq import heappush, heappop, nlargest, nsmallest
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
         pi, sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan
# sys.setrecursionlimit(5782)

print = functools_partial(print, flush=True)
input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'humble'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')







import time

def leetcode313(K, N, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    i = [0] * K # for each prime, index in humble s.t. humble[i[k]] * primes[k] is a candidate
    humble = [1]

    cands = [] # K candidates, among which the next min can be found
    for k in range(K):
        heappush(cands, (primes[k], k))

    N1 = N + 1
    while len(humble) < N1:
        cand, k = heappop(cands)
        if humble[-1] != cand:
            humble.append(cand)
        i[k] += 1
        heappush(cands, (humble[i[k]] * primes[k], k))

    return humble[-1]

ttt = time.time()

K, N = map(int, input().split())
ps = list(map(int, input().split()))
ps.sort()

printwrite(leetcode313(K, N, ps))









fin.close()
fout.close()
del print, input

print(time.time() - ttt)