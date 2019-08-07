"""
ID: wrwwctb1
LANG: PYTHON3
TASK: race3
4.3.3

key idea
a node u is unavoidable if
    removing u's out edges disconnects s and t

a node u is a splitting point if following are disjoint
    points reachable from s when u is removed
    points reachable from u

why doesn't max flow work?
max flow might go through a node that is not unavoidable

how about:
    a node is unavoidable if it is alone in a bfs level starting from s
"""

import os, sys, re
from collections import Counter, deque, defaultdict
from copy import copy, deepcopy
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

filename = 'race3'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')











def dfs(neigs, s):
    status = [0] * len(neigs) # 0: untouched. 1: in stack. 2: done
    stack = [s]
    status[s] = 1
    while stack:
        u = stack.pop()
        status[u] = 2
        for v in neigs[u]:
            if status[v] == 0:
                status[v] = 1
                stack.append(v)
    return status

def output(ls):
    out = [len(ls)] + ls
    out = ' '.join(map(str, out))
    printwrite(out)


# n <= 50
# m <= 100


neigs = []

u = 0
while True:
    line = list(map(int, input().split()))
    if line[0] == -1:
        break
    neigs.append(line[:-1])

unavoidable = []
cleanCut = []

for u in range(1, len(neigs)-1):
    neigsu = neigs[u]
    neigs[u] = []

    # dfs from s. stop at u if u is clean cut
    statusS = dfs(neigs, 0)
    if not all(statusS):
        unavoidable.append(u)


    # dfs from u
    neigs[u] = neigsu
    statusU = dfs(neigs, u)

    # check if statusS and statusU are complement
    sss = sum([s > 0 for s in statusS]) + \
          sum([s > 0 for s in statusU])

    if sss == len(neigs) + 1:
        cleanCut.append(u)

output(unavoidable)
output(cleanCut)










fin.close()
fout.close()
del print, input

