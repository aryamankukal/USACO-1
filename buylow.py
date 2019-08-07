"""
ID: wrwwctb1
LANG: PYTHON3
TASK: buylow
4.3.2

key idea
n^2 LIS. count sols. avoid repetition

recursive tracing gets too many
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

filename = 'buylow'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')











def LDS(a):
    L = [] # L[i]: ans that ends at i
    M = [] # M[i]: num of ways to assemble L[i]
    a.append(-1) # with this, ans will be L[-1]-1, M[-1]

    for i, ai in enumerate(a):
        # find longest previous
        best = 0
        for j in range(i):
            if a[j] > ai and best < L[j]:
                best = L[j]

        if best == 0: # ie not found
            L.append(1)
            M.append(1)
        else:
            # to count cases, avoid re-counting the same aj. give priority to
            # aj that appears later. consider 3 2 4 2
            L.append(best + 1)
            got = set()
            cnt = 0
            for j in range(i-1, -1, -1):
                if L[j] == best and a[j] > ai and a[j] not in got:
                    cnt += M[j]
                    got.add(a[j])
            M.append(cnt)

    # debug
#    print('%3d' * len(a) % tuple(a))
#    print('%3d' * len(L) % tuple(L))
#    print('%3d' * len(M) % tuple(M))

    return L[-1] - 1, M[-1]


N = int(input())
aa = []
while True:
    line = input()
    if line == '':
        break
    aa += list(map(int, line.split()))


bestL, cnt = LDS(aa)

printwrite('%d %d' % (bestL, cnt))











fin.close()
fout.close()
del print, input

