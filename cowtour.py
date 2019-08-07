"""
ID: wrwwctb1
LANG: PYTHON3
TASK: cowtour
2.4.4

key idea
floyd warshall
everything else takes less time:
    find components
    find diameters of components
    find, for each component, the max distance to each node
    try every pair of components
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

filename = 'cowtour'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')










def distfun(pt1, pt2):
    return hypot(pt1[0]-pt2[0], pt1[1]-pt2[1])

def pdist():
    for i in range(N):
        for j in range(N):
            print('%6.3f' % dist[i][j], end=' ')
        print('')

def floydwarshall(dist, N):
    # if not in a function, allotted time is not enough, even with optimization
    for x in range(N):
        # distx = dist[x]
        for u in range(N):
            for v in range(N):
                # newdist = distx[u] + distx[v] # assume dist[][] symmetric
                newdist = dist[u][x] + dist[x][v]
                if newdist < dist[u][v]:
                    dist[u][v] = newdist

def findcomponents(dist):
    compls = [None] * N
    comp = []
    for i in range(N):
        if compls[i] == None:
            compls[i] = len(comp)
            comp.append([i])
            for j in range(i+1, N):
                if dist[i][j] != inf:
                    compls[j] = compls[i]
                    comp[-1].append(j)

    assert all([i != None for i in compls])
    return comp

def finddiameters(comp, dist):
    # find diameter of each comp
    diameter = [-1] * len(comp)
    for c in range(len(comp)):
        for i in range(len(comp[c])):
            for j in range(i+1, len(comp[c])):
                cand = dist[comp[c][i]][comp[c][j]]
                assert cand != inf
                diameter[c] = max(diameter[c], cand)
    return diameter

def findLenThruNeck(comp, dist):
    # through: for each component, if every node goes out through a node, what is the farthest
    through = []
    for c in range(len(comp)):
        throughc = [max([dist[m][n] for n in comp[c]]) for m in comp[c]]
        through.append(throughc)
    return through

def pair(through, comp, dist):
    # pair nodes across components. check diameter every time
    best = inf

    for i in range(len(comp)):
        compi = comp[i]
        throughi = through[i]
        diameteri = diameter[i]

        for j in range(i+1, len(comp)):
            compj = comp[j]
            throughj = through[j]
            diameterj = diameter[j]

            maxdiameter = max(diameteri, diameterj)

            for m in range(len(compi)):

                ptcompim = pt[compi[m]]
                throughim = throughi[m]

                for n in range(len(compj)):

                    bridge = distfun(ptcompim, pt[compj[n]])
                    cand = throughim + bridge + throughj[n]
                    best = min(best, max(maxdiameter, cand))

    return best


N = int(input())
pt = []
for n in range(N):
    pt.append(list(map(int, input().split())))

adj01 = []
for n in range(N):
    line = input()
    adj01.append(line)

dist = [[inf] * N for n in range(N)]
for n in range(N):
    dist[n][n] = 0

for i in range(N):
    for j in range(i+1, N):
        if adj01[i][j] == '1':
            dist[i][j] = dist[j][i] = distfun(pt[i], pt[j])


floydwarshall(dist, N)

comp = findcomponents(dist)

diameter = finddiameters(comp, dist)

# through: for each component, if every node goes out through a node, what is the farthest
through = findLenThruNeck(comp, dist)

# pair nodes across components. check diameter every time
best = pair(through, comp, dist)

printwrite('%.6f' % best)










fin.close()
fout.close()
del print, input

