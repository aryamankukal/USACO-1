"""
ID: wrwwctb1
LANG: PYTHON3
TASK: telecow
5.4.3

key idea
to formulate min node cut as min edge cut
- every node is separated into in and out nodes
- original edges have cap inf
- cap 1 from in->out
- all back edges are set up as required in max flow


to find the specific cut
route 1
- after edmond karp, collect used edges, which are all in->out edges
- one loop, try each used edge, see if deleting it reduces max flow
route 2
- when entering cap, decorate as (1 << 13) + node#,
  so that smaller node#s are favored
- flood fill on residual graph after min cut
  if an in-node is visited but its out-node is not, the node is on the cut line



wrong formulation:
- every node is one node (no in/out nodes)
- every edge has cap 1
- after edmond karp, find nodes that are "saturated" ie all edges around it have a full flow
- try each saturated node, does deleting it affect max flow?
what's wrong:
- a wanted node might not be "saturated" after edmond karp
- deleting a wanted node might not reduce max flow
^ see saved telecow.in for examples
- greedily searching for a node, deleting which yields the highest reduction in max flow,
  does not give fewest # of nodes
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

filename = 'telecow'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')














def fattest(s, t, neigs, caps, N):


    pq = [(-inf, s)]
    est = [0] * (2*N+1)
    parent = [None] * (2*N+1)
    done = [False] * (2*N+1)

    while pq:
        uflow, u = heappop(pq)
        uflow *= -1

        if done[u]:
            continue

        done[u] = True

        if u == t:
            return uflow, parent

        for v in neigs[u]:
            if done[v]:
                continue

            cand = min(uflow, caps[u, v])
            if est[v] < cand:
                est[v] = cand
                parent[v] = u
                heappush(pq, (-cand, v))
    return 0, []

def edmondKarp(s, t, neigs, caps, N):
    tot = 0
    while True:
        flow, parent = fattest(s, t, neigs, caps, N)
        if flow == 0:
            break
        tot += flow


        # update residual graph
        v = t
        while v != s:
            u = parent[v]

            caps[u, v] -= flow
            caps[v, u] += flow
            v = u
    return tot

def show(caps):
    for cap in caps:
        print(cap)


N, M, s, t = map(int, input().split())
sN = s + N
tN = t + N # want in-node of s to go to out-node of t
inNodes = list(range(1, N+1))
neigs = [set() for n in range(2*N+1)] # out neighbors

caps0 = {} # matrix should be ok too
for u in range(1, N+1):
    caps0[u, u+N] = (1 << 13) + u
    caps0[u+N, u] = 0
    neigs[u].add(u+N)
    neigs[u+N].add(u) # back edge
for m in range(M):
    u, v = map(int, input().split())
    caps0[u+N, v] = inf
    caps0[v+N, u] = inf
    caps0[v, u+N] = 0 # back edges
    caps0[u, v+N] = 0
    neigs[u+N].add(v)
    neigs[v+N].add(u)
    neigs[v].add(u+N) # back edges
    neigs[u].add(v+N)

maxFlow = edmondKarp(sN, t, neigs, caps0, N)

# flood fill
stack = [s]
visited = [False] * (2 * N + 1)
while stack:
    u = stack.pop()
    visited[u] = True
    for v in neigs[u]:
        if visited[v] or caps0[u, v] == 0:
            continue
        stack.append(v)

cut = []
for u in range(1, N + 1):
    if visited[u] and not visited[u + N]:
        cut.append(u)

# output
printwrite(len(cut))
printwrite(' '.join(['%d'] * len(cut)) % tuple(cut))










fin.close()
fout.close()
del print, input

