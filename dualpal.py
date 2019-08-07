"""
ID: wrwwctb1
LANG: PYTHON3
TASK: dualpal
1.3.6
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

filename = 'dualpal'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')



def changebases(n, B):
    out = []
    while n > 0:
        n, rem = divmod(n, B)
        out.append(rem)
    return out[::-1]

def check(n):
    cnt = 0
    for B in range(2, 11):
        nB = changebases(n, B)
        if nB[-1] == 0:
            continue
        else:
            if nB == nB[::-1]:
                cnt += 1
                if cnt >= 2:
                    return True
    return False

N, S = input().split()
N = int(N)
S = int(S)
cnt = 0
curr = S + 1
while cnt < N:
    if check(curr):
        cnt += 1
        printwrite(curr)

    curr += 1





fin.close()
fout.close()
del print, input

