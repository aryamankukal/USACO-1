"""
ID: wrwwctb1
LANG: PYTHON3
TASK: comehome
2.4.5

point 1/2

dijkstra est can be list or dict

but these are only for dict:
    "v not in est"
    "cow in shortestpath"

point 2/2

descriptions need to be read in the most pedantic way
"""

import os, sys, re, itertools, functools
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
input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'comehome'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')








# ok
def dijkm(mat, zz):
    pq = [(0, zz)]
    done = set()
    est = [inf] * 52
    est[zz] = 0

    while pq:
        pathlen, u = heappop(pq)

        if u in done:
            continue

        done.add(u)

        for v in range(52):
            if v in done:
                continue

            if pathlen + mat[u][v] < est[v]:
                newpathlen = pathlen + mat[u][v]
                est[v] = newpathlen
                heappush(pq, (newpathlen, v))

    return est

# ok
def dijk(neig, zz):
    pq = [(0, zz)]
    done = set()
    est = {zz: 0}

    while pq:
        pathlen, u = heappop(pq)

        if u in done:
            continue

        done.add(u)

        for w, v in neig[u]:
            if v in done:
                continue

            if v not in est or pathlen + w < est[v]:
                newpathlen = pathlen + w
                est[v] = newpathlen
                heappush(pq, (newpathlen, v))

    return est

def ch2n(ch):
    if str.isupper(ch):
        return ord(ch) - ord('A') + 26
    else:
        return ord(ch) - ord('a')




P = int(input())

neig = [[] for i in range(52)]
#mat = [[inf] * 52 for i in range(52)]

for p in range(P):
    u, v, w = input().split()
    w = int(w)

    u = ch2n(u)
    v = ch2n(v)

    # make connections
    neig[u].append((w, v))
    neig[v].append((w, u))

#    mat[u][v] = mat[v][u] = min(mat[u][v], w)



shortestpath = dijk(neig, ch2n('Z'))
#shortestpath = dijkm(mat, ch2n('Z'))

earliestcow = None
earliesttime = inf
for cow in range(ch2n('A'), ch2n('Y')+1):
    if cow in shortestpath and shortestpath[cow] < earliesttime:
    #if shortestpath[cow] < earliesttime:
        earliesttime = shortestpath[cow]
        earliestcow = cow

earliestcow = 'ABCDEFGHIJKLMNOPQRSTUVWXY'[earliestcow-ch2n('A')]

printwrite('%s %d' % (earliestcow, earliesttime))








fin.close()
fout.close()
del print, input

