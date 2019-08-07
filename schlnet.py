"""
ID: wrwwctb1
LANG: PYTHON3
TASK: schlnet
5.3.4

key ideas
task 1:     scc -> dag. each *root* super node in dag should get software
task 2:     wrong: each leaf in dag needs an extension
            right: num of required extensions = max(numRoots, numLeaves)
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

filename = 'schlnet'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')














def topoSort_help(R, u, T, prog, endT):
    # start time T
    prog[u] = 1
    T += 1
    for v in R[u]:
        if prog[v] == 0:
            T = topoSort_help(R, v, T, prog, endT)
    endT[u] = T
    prog[u] = 2
    return T + 1 # return end time + 1

def topoSort(R):
    N1 = len(R)
    endT = [0] * N1 # end time cannot be 0
    prog = [0] * N1 # 0 unvisited 1 in progerss 2 finished
    T = 0
    for u in range(1, N1):
        if prog[u] == 0:
            T = topoSort_help(R, u, T, prog, endT)
#    print(prog, endT)
    return endT

def findOneSCC(G, SCC, prog, u):
    prog[u] = 1
    for v in G[u]:
        if prog[v] == 0:
            findOneSCC(G, SCC, prog, v)
    prog[u] = 2
    SCC.append(u)

def findSCCs(G, endTu):
    # find scc, seed has decreasing end time found by topoSort
    N1 = len(G)
    prog = [0] * N1 # 0 unvisited 1 in progress 2 finished
    SCCs = []
    for u in endTu[:-1]:
        if prog[u] == 0:
            oneSCC = []
            findOneSCC(G, oneSCC, prog, u)
            SCCs.append(oneSCC)
    return SCCs



N = int(input())
G = [[]]
R = [[] for n in range(N+1)] # reversed edge graph
for u in range(1, N+1):
    line = list(map(int, input().split()))[:-1]
    G.append(line)
    for v in line:
        R[v].append(u)

endT = topoSort(R)

endTu = sorted(range(N+1), key=lambda i: endT[i], reverse=True)

SCCs = findSCCs(G, endTu)

node2super = [None] * (N+1)
for superNode, SCC in enumerate(SCCs):
#    print(superNode, SCC)
    for u in SCC:
        node2super[u] = superNode

# check if each super node has in neig or out neig
inN = [False] * len(SCCs)
ouN = [False] * len(SCCs)
for u in range(1, N+1):
    for v in G[u]:
        super_u = node2super[u]
        super_v = node2super[v]
        if super_u != super_v:
            ouN[super_u] = True
            inN[super_v] = True

numRoots = sum([not hasInN for hasInN in inN])
printwrite(numRoots)
if len(SCCs) == 1:
    printwrite(0)
else:
    numLeaves = sum([not hasOuN for hasOuN in ouN])
    printwrite(max(numRoots, numLeaves))







fin.close()
fout.close()
del print, input

