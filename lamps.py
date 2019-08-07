"""
ID: wrwwctb1
LANG: PYTHON3
TASK: lamps
2.2.6

key idea
order doesn't matter
one switch only has two possible effects on the outcome: pressed 0 or 1 time
but if total count of presses C < 3, not all states are accessible
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

filename = 'lamps'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')






def genstates(N):
    NN = 4
    out = [set() for n in range(NN+1)]
    for i in range(NN+1):
        for j in range(NN+1):
            for k in range(NN+1):
                for l in range(NN+1):
                    state = [1] * N
                    # toggle all
                    for ii in range(i % 2):
                        for x in range(N):
                            state[x] = 1 - state[x]
                    # toggle odd
                    for jj in range(j % 2):
                        for x in range(0, N, 2): # 0th is "first"
                            state[x] = 1 - state[x]
                    # toggle even
                    for kk in range(k % 2):
                        for x in range(1, N, 2): # 1th is "second"
                            state[x] = 1 - state[x]
                    # toggle 1 4 7
                    for ll in range(l % 2):
                        for x in range(0, N, 3):
                            state[x] = 1 - state[x]
                    s = i+j+k+l
                    if s <= 4:
                        out[s].add((''.join(map(str, state))))

    for x in range(len(out)):
        out[x] = sorted(list(out[x]))
    return out

N = int(input())
C = int(input())
ons = list(map(int, input().split()[:-1]))
ofs = list(map(int, input().split()[:-1]))

out = genstates(N)
#for o in out:
#    print(o)

pattern = ['.'] * N
for onpos in ons:
    pattern[onpos-1] = '1'
for ofpos in ofs:
    pattern[ofpos-1] = '0'
pattern = ''.join(pattern)

if C > 3:
    C = 3

printflag = False
for poss in out[C]:
    if re.fullmatch(pattern, poss):
        printflag = True
        printwrite(poss)

if printflag == False:
    printwrite('IMPOSSIBLE')





fin.close()
fout.close()
del print, input

