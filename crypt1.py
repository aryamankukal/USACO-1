"""
ID: wrwwctb1
LANG: PYTHON3
TASK: crypt1
1.4.5
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

filename = 'crypt1'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')



def check(n, d):
    while n > 0:
        n, rem = divmod(n, 10)
        if rem not in d:
            return False
    return True




N = int(input())
d = list(map(int, input().split()))
d.sort()

# check all possibilities

mx = 100 * d[-1] + 10 * d[-1] + d[-1]
cnt = 0
for t0 in range(N):

    for b0 in range(N):
        # filter?

        for t1 in range(N):
            # filter?

            for b1 in range(N):
#                if d[b1] == 0:
#                    continue

                bot = 10 * d[b1] + d[b0]


                for t2 in range(N):
#                    if d[t2] == 0:
#                        continue
                    top = 100 * d[t2] + 10 * d[t1] + d[t0]

                    p1 = top * d[b0]
                    if p1 > mx:
                        continue

                    if not check(p1, d):
                        continue

                    p2 = top * d[b1]
                    if p2 > mx:
                        continue

                    if not check(p2, d):
                        continue

                    m = p2 * 10 + p1
                    if not check(m, d):
                        continue
                    #assert top * bot == m
                    #print(top, bot, p1, p2, m)
                    cnt += 1
printwrite(cnt)

fin.close()
fout.close()
del print, input

