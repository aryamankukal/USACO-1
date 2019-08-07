"""
ID: wrwwctb1
LANG: PYTHON3
TASK: vans
6.1.1

key idea
dp
f = [0] * (N+1) # num of ways, n cols, [1, 1] to [2, 1] or reverse
g = [0] * (N+1) # num of ways, n cols, [1, 1] to [4, 1] or reverse
ans = f[-1]


see note for def of g1 g2 g3 g4

f [i] = f [i-1] + g [i-1]
g [i] = g1[i  ] + g2[i  ] + g3[i  ] + g4[i  ]

g1[i] = f[i-1]
g2[i] = f[i-1]
g3[i] = g[i-2]
g4[i] = g4[i-1] + f [i-2] + f [i-2]
      = g [i-1] - g1[i-1] - g2[i-1] - g3[i-1] + f [i-2] * 2
      = g [i-1] - f [i-2] - f [i-2] - g [i-3] + f [i-2] * 2
      = g [i-1] - g [i-3]

g [i]
= g1[i  ] + g2[i  ] + g3[i  ] + g4[i  ]
= f [i-1] + f [i-1] + g [i-2] + g [i-1] - g [i-3]
= f [i-1] * 2       + g [i-1] + g [i-2] - g [i-3]

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

filename = 'vans'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









N = int(input())
if N <= 4:
    if N == 1:
        printwrite(0)
    elif N == 2:
        printwrite(2)
    elif N == 3:
        printwrite(4)
    else: # 4
        printwrite(12)
else:
    f = [0] * (N+1) # num of ways, n cols, [1, 1] to [2, 1] or reverse
    g = [0] * (N+1) # num of ways, n cols, [1, 1] to [4, 1] or reverse
    f[1] = 0
    f[2] = 2
    f[3] = 4
    g[1] = 2
    g[2] = 2
    g[3] = 8

    for n in range(4, N+1):


        g[n] = f[n-1] * 2 + g[n-1] + g[n-2] - g[n-3]
        f[n] = f[n-1] + g[n-1]


    printwrite(f[N])










fin.close()
fout.close()
del print, input

