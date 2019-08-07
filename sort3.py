"""
ID: wrwwctb1
LANG: PYTHON3
TASK: sort3
2.1.5

key idea
only two kinds of swaps are required
1 swap for each 1-to-1 mix up
2 swaps for each 3-way mix up
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

filename = 'sort3'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')







def look(ls, rf, a, b):
    assert a < b
    cnt = 0
    m = 0
    n = None
    while True:
        while m < len(ls):
            if rf[m] == a and ls[m] == b:
                break
            m += 1

        if n == None:
            n = m + 1
        else:
            n = max(n, m + 1)

        while n < len(ls):
            if rf[n] == b and ls[n] == a:
                break
            n += 1

        if n < len(ls) and m < len(ls):
            m += 1
            n += 1
            cnt += 1
        else:
            return cnt

N = int(input())
ls0 = []
for n in range(N):
    ls0.append(int(input()))

cnter = Counter(ls0)
rf0 = []
for key, val in sorted(cnter.items()):
    rf0 += [key] * val

# count correct ones
cntCorrect = 0
for n in range(N):
    if ls0[n] == rf0[n]:
        cntCorrect += 1

cnt = 0
cnt += look(ls0, rf0, 1, 2)
cnt += look(ls0, rf0, 2, 3)
cnt += look(ls0, rf0, 1, 3)

notDone = len(ls0) - cntCorrect - cnt * 2
assert notDone % 3 == 0
cnt += (notDone // 3) * 2

printwrite(cnt)




fin.close()
fout.close()
del print, input

