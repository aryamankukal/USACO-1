"""
ID: wrwwctb1
LANG: PYTHON3
TASK: castle
2.1.3
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

filename = 'castle'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')






# if wall
def west(m):
    return m & 1
def north(m):
    return m & 2
def east(m):
    return m & 4
def south(m):
    return m & 8

def floodfill(castle):
    N = len(castle)
    M = len(castle[0])

    compmap = [[-1] * M for n in range(N)]
    maxsize = -1 # return size of largest room
    compnum = 0
    sizes = []
    for n in range(N):
        for m in range(M):
            if compmap[n][m] == -1:
                compsize = helper_recursive(castle, n, m, compmap, compnum)
                sizes.append(compsize)
                maxsize = max(maxsize, compsize)
                compnum += 1
    return maxsize, compnum, sizes, compmap

def helper_recursive(castle, n, m, compmap, compnum):
    # dfs post-order
    N = len(castle)
    M = len(castle[0])

    module = castle[n][m]
    compmap[n][m] = compnum
    compsize = 1
    if m-1 >= 0 and compmap[n][m-1] == -1 and not west(module):
        foundcompsize = helper_recursive(castle, n, m-1, compmap, compnum)
        compsize += foundcompsize
    if n-1 >= 0 and compmap[n-1][m] == -1 and not north(module):
        foundcompsize = helper_recursive(castle, n-1, m, compmap, compnum)
        compsize += foundcompsize
    if m+1 < M and compmap[n][m+1] == -1 and not east(module):
        foundcompsize = helper_recursive(castle, n, m+1, compmap, compnum)
        compsize += foundcompsize
    if n+1 < N and compmap[n+1][m] == -1 and not south(module):
        foundcompsize = helper_recursive(castle, n+1, m, compmap, compnum)
        compsize += foundcompsize
    return compsize

def helper(castle, nn, mm, compmap, compnum):
    # dfs in-order
    N = len(castle)
    M = len(castle[0])

    st = [(nn, mm)] # stack
    compsize = 0
    while len(st) > 0:
        n, m = st.pop()
        module = castle[n][m]
        compmap[n][m] = compnum
        compsize += 1
        if m-1 >= 0 and compmap[n][m-1] == -1 and not west(module):
            st.append((n, m-1))
            compmap[n][m-1] = -2
        if n-1 >= 0 and compmap[n-1][m] == -1 and not north(module):
            st.append((n-1, m))
            compmap[n-1][m] = -2
        if m+1 < M and compmap[n][m+1] == -1 and not east(module):
            st.append((n, m+1))
            compmap[n][m+1] = -2
        if n+1 < N and compmap[n+1][m] == -1 and not south(module):
            st.append((n+1, m))
            compmap[n+1][m] = -2
    return compsize

def breakawall(castle, sizes, compmap):
    N = len(castle)
    M = len(castle[0])
    best = -1
    bestparams = (0,) * 3
    for m in range(M):
        for n in range(N-1, -1, -1):
            module = castle[n][m]
            # n first
            if 0 < n and north(module) and compmap[n][m] != compmap[n-1][m]:
                cand = sizes[compmap[n][m]] + sizes[compmap[n-1][m]]
                if cand > best:
                    best = cand
                    bestparams = n+1, m+1, 'N'
            # then e
            if m < M - 1 and east(module) and compmap[n][m] != compmap[n][m+1]:
                cand = sizes[compmap[n][m]] + sizes[compmap[n][m+1]]
                if cand > best:
                    best = cand
                    bestparams = n+1, m+1, 'E'
    return best, bestparams

def visualize(castle):
    N = len(castle)
    M = len(castle[0])
    for n in range(N):
        for m in range(M):
            module = castle[n][m]
            if west(module):
                ch1 = '|'
            else:
                ch1 = ' '
            if east(module):
                ch3 = '|'
            else:
                ch3 = ' '
            if north(module) and south(module):
                ch2 = 'I'
            elif north(module) and not south(module):
                ch2 = '?'
            elif not north(module) and south(module):
                ch2 = '_'
            else:
                ch2 = ' '
            print('%s%s%s' % (ch1, ch2, ch3), end='')
        print('')


#import time
#tt = time.time()


M, N = map(int, input().split())
castle = []
for n in range(N):
    row = list(map(int, input().split()))
    castle.append(row)


maxsize, numcomps, sizes, compmap = floodfill(castle)

best, bestparams = breakawall(castle, sizes, compmap)

printwrite('%d\n%d\n%d\n%d %d %s' % ((numcomps, maxsize, best)+bestparams))







fin.close()
fout.close()
del print, input


#print(time.time()-tt)
