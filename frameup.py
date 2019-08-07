"""
ID: wrwwctb1
LANG: PYTHON3
TASK: frameup
4.4.3

key idea
recursively find all topological sort
when choosing the next frame, any frame that is not covered can be a cand
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

filename = 'frameup'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')














def checkTopo(outNeigs, inDeg, arr, top, lef, bot, rig, curr):
    ouN = set()
    t = top[curr]
    l = lef[curr]
    b = bot[curr]
    r = rig[curr]
    for j in range(l, r+1):
        if arr[t][j] != curr:
            ouN.add(arr[t][j])
        if arr[b][j] != curr:
            ouN.add(arr[b][j])
    for i in range(t, b+1):
        if arr[i][l] != curr:
            ouN.add(arr[i][l])
        if arr[i][r] != curr:
            ouN.add(arr[i][r])

    outNeigs[curr] = ouN
    for neig in ouN:
        inDeg[neig] += 1

def allTopoSortHelper(outNeigs, inDeg, visited, currHistory, out):
    ifEnd = True
    for u in inDeg.keys():
        if inDeg[u] == 0 and visited[u] == False:
            ifEnd = False

            visited[u] = True
            for v in outNeigs[u]:
                inDeg[v] -= 1
            currHistory.append(u)

            allTopoSortHelper(outNeigs, inDeg, visited, currHistory, out)

            del currHistory[-1]
            for v in outNeigs[u]:
                inDeg[v] += 1
            visited[u] = False
    if ifEnd:
        out.append(''.join(currHistory))

def allTopoSort(outNeigs, inDeg):
    visited = {}
    for u in inDeg.keys():
        visited[u] = False
    out = []
    allTopoSortHelper(outNeigs, inDeg, visited, [], out)
    return out


H, W = map(int, input().split())
arr = []
for h in range(H):
    line = input()
    arr.append([ch for ch in line])

# find extend of all
top = {}
lef = {}
bot = {}
rig = {}

for h in range(H):
    for w in range(W):
        if arr[h][w] != '.':
            if arr[h][w] in top:
                top[arr[h][w]] = min(top[arr[h][w]], h)
                lef[arr[h][w]] = min(lef[arr[h][w]], w)
                bot[arr[h][w]] = max(bot[arr[h][w]], h)
                rig[arr[h][w]] = max(rig[arr[h][w]], w)
            else:
                top[arr[h][w]] = h
                lef[arr[h][w]] = w
                bot[arr[h][w]] = h
                rig[arr[h][w]] = w

# make topological graph
outNeigs = {}
inDeg = {}
for key in top.keys():
    inDeg[key] = 0

for curr in top.keys():
    checkTopo(outNeigs, inDeg, arr, top, lef, bot, rig, curr)

out = allTopoSort(outNeigs, inDeg)

out.sort()

for ou in out:
    printwrite(ou)













fin.close()
fout.close()
del print, input

