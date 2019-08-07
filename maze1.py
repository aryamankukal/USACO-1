"""
ID: wrwwctb1
LANG: PYTHON3
TASK: maze1
2.4.3

key idea
combine the two entrances as one source node, bfs to find the farthest node
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

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

print = functools.partial(print, flush=True)
input = lambda: fin.readline().strip('\n')

filename = 'maze1'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









def findentrances(W, H, mp):
    ilist = [0] * (2*W+1) + list(range(1, 2*H+1)) + \
            [2*H] * (2*W) + list(range(2*H-1, 0, -1))
    jlist = list(range(2*W+1)) + [2*W] * (2*H) + \
            list(range(2*W-1, -1, -1)) + [0] * (2*H-1)
#    assert len(ilist) == len(jlist)
#    for x in range(len(ilist)):
#        print(ilist[x], jlist[x])
    found = []
    for x in range(len(ilist)):
        if mp[ilist[x]][jlist[x]] == ' ':
            found.append((ilist[x], jlist[x]))
    assert len(found) == 2
    return found


def findfirstneigs(entrances, W, H, mp):
    neigs = []
    for i, j in entrances:
        if i == 0:
            neigs.append((i+1, j))
        elif i == 2*H:
            neigs.append((i-1, j))
        elif j == 0:
            neigs.append((i, j+1))
        elif j == 2*W:
            neigs.append((i, j-1))
        else:
            assert False
    return neigs

def findneigs(loc, W, H, mp):
    neigs = []
    i, j = loc
    # n
    if i > 1 and mp[i-1][j] == ' ':
        neigs.append((i-2, j))
    # s
    if i < 2*H-1 and mp[i+1][j] == ' ':
        neigs.append((i+2, j))
    # e
    if j < 2*W-1 and mp[i][j+1] == ' ':
        neigs.append((i, j+2))
    # w
    if j > 1 and mp[i][j-1] == ' ':
        neigs.append((i, j-2))
    return neigs

def showmp():
    for line in mp:
        for ch in line:
            print(ch, end='')
        print('')

W, H = map(int, input().split())
mp = []
for h in range(2*H+1):
    line = input()
    line = [ch for ch in line]
    mp.append(line)

entrances = findentrances(W, H, mp)
firstneigs = findfirstneigs(entrances, W, H, mp)
#print(neigs)
#neigs = findneigs(neigs[1], W, H, mp)
#print(neigs)

qq = deque()
qq.append((1, firstneigs[0]))
qq.append((1, firstneigs[1]))
mp[firstneigs[0][0]][firstneigs[0][1]] = 'x'
mp[firstneigs[1][0]][firstneigs[1][1]] = 'x'


maxlevel = -1
while len(qq) > 0:
    level, loc = qq.popleft()
    maxlevel = max(maxlevel, level)
    neigs = findneigs(loc, W, H, mp)
    level += 1
    for neig in neigs:
        if mp[neig[0]][neig[1]] != 'x':
            qq.append((level, neig))
            mp[neig[0]][neig[1]] = 'x'

printwrite(maxlevel)










fin.close()
fout.close()
del print, input

