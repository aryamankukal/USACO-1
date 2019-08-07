"""
ID: wrwwctb1
LANG: PYTHON3
TASK: fence6
4.1.3

key idea
for e in all edges:
    delete e
    dijkstra from an end point
    loop perimeter = dijkstra result + length of e
    update min perimeter

detecting all simple cycles is no joke. but we don't need to

why doesn't "dfs with cycle detection" work? does it on paper?
stick to all game plans: short-term, mid-term, and long-term
"""

import os, sys, re
from collections import Counter, deque, defaultdict
from copy import copy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key, partial as functools_partial
from heapq import heappush, heappop, nlargest, nsmallest
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
         pi, sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan
# sys.setrecursionlimit(5782)

print = functools_partial(print, flush=True)
input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'fence6'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')

















class Edge:
    def __init__(self, L, N1, N2):
        self.L = L
        self.N1 = N1
        self.N2 = N2
        self.neigu = []
        self.neigv = []
        self.u = None
        self.v = None
    def __repr__(self):
        s = '%d %d %d ' % (self.L, self.N1, self.N2)
        s += str(self.neigu)
        s += str(self.neigv)
        return s

class Node:
    def __init__(self):
        self.neig = {} # neig[neigname] = weight

    def __repr__(self):
        s = str(self.neig)
        return s

def dijk(nodes, s, t):
    pq = [(0, s)]
    est = {}
    done = set()

    while pq:
        p, u = heappop(pq)

        if u in done:
            continue

        if u == t:
            return p

        done.add(u)

        for v, l in nodes[u].neig.items():
            if v in done:
                continue

            if v not in est or p + l < est[v]:
                est[v] = cand = p + l
                heappush(pq, (cand, v))
    return inf


# input, minimal processing
N = int(input())
edges = {} # edges[name] = obj   e=name    E=obj
for n in range(N):
    e, L, N1, N2 = map(int, input().split())
    E = Edge(L, N1, N2)
    E.neigu.extend(list(map(int, input().split())))
    E.neigv.extend(list(map(int, input().split())))
    edges[e] = E


# identify nodes
nodes = {} # nodes[name] = obj. node name is its surrounding edges
for e, E in edges.items():
    # node name = sorted edge names, not including edgetoskip
    u = tuple(sorted(set(E.neigu + [e])))
    v = tuple(sorted(set(E.neigv + [e])))
    E.u = u
    E.v = v
    if u not in nodes:
        nodes[u] = Node()
    if v not in nodes:
        nodes[v] = Node()

best = inf
for edgetoskip in edges:
    # set up neighbors. exclude edgetoskip
    for u, U in nodes.items():
        U.neig = {}

        for e in u:
            if e == edgetoskip:
                continue
            E = edges[e]
            edgeu = E.u
            edgev = E.v
            edgelen = E.L
            if u == edgeu:
                U.neig[edgev] = edgelen
            else:
                assert u == edgev
                U.neig[edgeu] = edgelen

    Edgetoskip = edges[edgetoskip]
    cand = dijk(nodes, Edgetoskip.u, Edgetoskip.v) + Edgetoskip.L
    if cand < best:
        best = cand

printwrite(best)












fin.close()
fout.close()
del print, input

