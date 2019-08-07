"""
ID: wrwwctb1
LANG: PYTHON3
TASK: ttwo
2.4.2
"""

import os, sys, re, itertools, functools, heapq
from collections import Counter, deque, defaultdict
from copy import copy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key
from heapq import heappush, heappop, nlargest, nsmallest
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
             sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan
# sys.setrecursionlimit(5782)

print = functools.partial(print, flush=True)
input = lambda: fin.readline().strip()

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'ttwo'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')





NN = 10

def step(i, j, d, mp):
    if d == 'n':
        if i == 0 or mp[i-1][j] == '*':
            d = 'e'
        else:
            i -= 1
    elif d == 's':
        if i == NN-1 or mp[i+1][j] == '*':
            d = 'w'
        else:
            i += 1
    elif d == 'e':
        if j == NN-1 or mp[i][j+1] == '*':
            d = 's'
        else:
            j += 1
    else: # d == 'w':
        if j == 0 or mp[i][j-1] == '*':
            d = 'n'
        else:
            j -= 1
    return i, j, d




mp = []
for i in range(NN):
    line = input()
    foundf = line.find('F')
    foundc = line.find('C')
    if foundf == -1 and foundc == -1:
        mp.append(line)
    else:
        if foundf != -1:
            fi, fj, fd = i, foundf, 'n'
            line = line.replace('F', '.')
        if foundc != -1:
            ci, cj, cd = i, foundc, 'n'
            line = line.replace('C', '.')
        mp.append(line)

#print(mp)

seen = set()
cnt = 0
ifmeet = False
while True:
    state = fi, fj, fd, ci, cj, cd
    if state in seen:
        break
    seen.add(state)
    if fi == ci and fj == cj:
        printwrite(cnt)
        ifmeet = True
        break

    fi, fj, fd = step(fi, fj, fd, mp)
    ci, cj, cd = step(ci, cj, cd, mp)
    cnt += 1

if not ifmeet:
    printwrite(0)






fin.close()
fout.close()
del print, input

