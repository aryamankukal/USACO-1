"""
ID: wrwwctb1
LANG: PYTHON3
TASK: starry
5.1.3
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

filename = 'starry'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









#def flatten(patch):
#    out = []
#    for row in patch:
#        out.extend(row)
#    return out

def fliplr(patch):
    out = []
    for row in patch:
        out.append(row[::-1])
    return tuple(out)

def fliptb(patch):
    return patch[::-1]

def transpose(patch):
    return tuple(zip(*patch))

def neighbors(sky, H, W, i, j):
    if i != 0 and sky[i-1][j] == 1:
        yield i-1, j
    if j != 0 and sky[i][j-1] == 1:
        yield i, j-1
    if i != H-1 and sky[i+1][j] == 1:
        yield i+1, j
    if j != W-1 and sky[i][j+1] == 1:
        yield i, j+1

    if i != 0 and j != 0 and sky[i-1][j-1] == 1:
        yield i-1, j-1
    if i != 0 and j != W-1 and sky[i-1][j+1] == 1:
        yield i-1, j+1
    if i != H-1 and j != W-1 and sky[i+1][j+1] == 1:
        yield i+1, j+1
    if i != H-1 and j != 0 and sky[i+1][j-1] == 1:
        yield i+1, j-1

def tuple2(patch):
    out = []
    for row in patch:
        out.append(tuple(row))
    return tuple(out)

def dfs(sky, H, W):
    knownPatches = {}
    ch = ord('a')
    for i in range(H):
        for j in range(W):
            if sky[i][j] == 1:
                # dfs find cluster
                sky[i][j] = 2 # in progress
                stack = [(i, j)]
                cluster = [(i, j)]
                while stack:
                    p, q = stack.pop()
                    for u, v in neighbors(sky, H, W, p, q):
                        sky[u][v] = 2
                        stack.append((u, v))
                        cluster.append((u, v))

                # build patch w/o topological mess
                Hm = inf
                HM = -1
                Wm = inf
                WM = -1
                for p, q in cluster:
                    Hm = min(p, Hm)
                    HM = max(p, HM)
                    Wm = min(q, Wm)
                    WM = max(q, WM)
                patch = [[0] * (WM - Wm + 1) for h in range(HM- Hm + 1)]
                for p, q in cluster:
                    p -= Hm
                    q -= Wm
                    patch[p][q] = 1
                patch = tuple2(patch)


                # check if patch is known
                if patch in knownPatches:
                    toFill = knownPatches[patch]
                else:
                    toFill = chr(ch)
                    ch += 1
                    # update knownPatches
                    lr = fliplr(patch)
                    tb = fliptb(patch)
                    rot180 = fliptb(lr)
                    tr = transpose(patch)
                    trlr = fliplr(tr)
                    trtb = fliptb(tr)
                    tr180 = fliptb(trlr)

                    knownPatches[patch]  = toFill
                    knownPatches[lr]     = toFill
                    knownPatches[tb]     = toFill
                    knownPatches[rot180] = toFill
                    knownPatches[tr]     = toFill
                    knownPatches[trlr]   = toFill
                    knownPatches[trtb]   = toFill
                    knownPatches[tr180]  = toFill

                # write cluster
                for p, q in cluster:
                    sky[p][q] = toFill

W = int(input())
H = int(input())
sky = []
for h in range(H):
    line = input()
    row = [int(ch) for ch in line]
    sky.append(row)

if W != 0 and H != 0:
    dfs(sky, H, W)

    for row in sky:
        rowOut = ''.join(map(str, row))
        printwrite(rowOut)










fin.close()
fout.close()
del print, input

