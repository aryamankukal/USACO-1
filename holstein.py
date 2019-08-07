"""
ID: wrwwctb1
LANG: PYTHON3
TASK: holstein
2.1.6

key idea
try all combinations. when checking, quit early if any vitamin is insufficient
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

filename = 'holstein'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')







V = int(input())
need = list(map(int, input().split()))
G = int(input())
scoop = []
for g in range(G):
    scoop.append(list(map(int, input().split())))

scoop = list(zip(*scoop))
indices = [g for g in range(G)]
for num in range(1, G+1):
    flag = False
    for comb in combinations(indices, num):
        flag_comb = True
        for v in range(V):
            scoop_v = scoop[v]
            has_v = sum([scoop_v[g] for g in comb])
            if has_v < need[v]:
                flag_comb = False
                break
        if flag_comb:
            flag = True
            break

    if flag:
        break
# output
printwrite(' '.join(['%d'] * (num+1)) % tuple([num] + [c+1 for c in comb]))






fin.close()
fout.close()
del print, input

