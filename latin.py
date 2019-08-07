"""
ID: wrwwctb1
LANG: PYTHON3
TASK: latin
6.5.1

review

very brutal

n            Tn                     An
2             1    2!                2

              2                      6

3             2    3!               12

             12                     48

4            24    4!              576

             56                    280

5          1344    5!           161280

            840                   5040

6       1128960    6!        812851200 (?)

    indivisible            indivisible

7   12198297600    7!   61479419904000 (?)

Let
An be num of latin sq of size n
Tn be num of latin sq of size n where row 1 is 1 2 ... n
Ln be num of latin sq of size n where both row 1 and col 1 are 1 2 ... n

An = Tn * n!             (permuting cols    of Tn gives An)

Tn = Ln * (n - 1)!       (permuting row 2-n of Ln gives Tn)

Calc Ln to get Tn

core logic: Ln(). ******avoid nested recursion if possible******

original version: Ln_help. >6min for N=7

tricky memoization: Ln3_help ~5s for N=7

what defines a state?

the following cases (top two rows shown) can all be characterized as (2, 3)
only need to calculate beyond two rows for one case

1 2 3 4 5
2 4 5 1 3

1 2 3 4 5
2 5 4 3 1

1 2 3 4 5
2 1 5 3 4
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

filename = 'latin'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')







class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None
    def __repr__(self):
        out = [str(self.val)]
        if self.nxt:
            out.append(self.nxt.__repr__())
        return ' '.join(out)

def createList(N, skip):
    root = Node(-1)
    curr = root
    for n in range(1, N+1):
        if n == skip:
            continue
        curr.nxt = Node(n)
        curr = curr.nxt
    return root

def Ln(roots, occ, N, row=2, col=2):
    '''
    recursively calc Ln
    row, col are current progress
    '''

#    if col == N + 1:
#        assert not roots[row].nxt
#        if row == N - 1: # the last row always has one choice. no need to call
#            return 1
#        else:
#            return Ln(row + 1)

    if col == N + 1:
        if row == N - 1:
            return 1
        row += 1
        col = 2


    prev = roots[row]
    curr = roots[row].nxt
    cnt = 0
    while curr:
        if occ[curr.val][col]: # if val not in col yet
            occ[curr.val][col] = 0
            prev.nxt = curr.nxt # could be None. remove from linked list

            cnt += Ln(roots, occ, N, row, col + 1)

            prev.nxt = curr
            occ[curr.val][col] = 1

        prev = curr
        curr = curr.nxt
    return cnt

def Ln_help(N):
    if N == 2:
        return 1

    roots = [None] * (N + 1)
    for n in range(2, N + 1):
        roots[n] = createList(N, n)

    occ = [[1] * (N + 1) for n in range(N+1)] # 0 if val occupies col
    for n in range(1, N + 1):
        occ[n][n] = 0

    return Ln(roots, occ, N)

def checkGroups(row2):
    N = len(row2) - 1
    seen = [False] * (N + 1)
    groups = []

    group = [1]
    seen[1] = True
    cur = 1
    while True:
        nxt = row2[cur]
        if nxt == group[0]:
            groups.append(len(group))
            firstUnseen = 2
            while firstUnseen <= N and seen[firstUnseen]:
                firstUnseen += 1
            if firstUnseen > N:
                break
            group = [firstUnseen]
            seen[firstUnseen] = True
            cur = firstUnseen
        else:
            group.append(nxt)
            seen[nxt] = True
            cur = nxt

    # simple hash
    hsh = 0
    for i, g in enumerate(sorted(groups)):
        hsh += (1 << 3*i) * g # ok because Nmax = 7
    return hsh

    #return tuple(sorted(groups))

def notGoodPerm(perm, N):
    for i, v in enumerate(perm):
        if v == i + 2:
            return True
    return False

def Ln3_help(N):
    if N == 2 or N == 3:
        return 1

    roots = [None] * (N + 1)
    for n in range(3, N + 1):
        roots[n] = createList(N, n)

    occ = [[1] * (N + 1) for n in range(N+1)] # 0 if val occupies col
    for n in range(1, N + 1):
        occ[n][n] = 0
    occ[2][1] = 0

    memo = {}

    cnt = 0
    for perm in permutations([1] + list(range(3, N + 1))): # first row
        if notGoodPerm(perm, N):
            continue

        row2 = [-1, 2] + list(perm)

        groupsHash = checkGroups(row2)

        if groupsHash not in memo:
            for i, v in enumerate(perm):
                occ[v][i+2] = 0

            memo[groupsHash] = Ln(roots, occ, N, 3, 2)

            for i, v in enumerate(perm):
                occ[v][i+2] = 1

        cnt += memo[groupsHash]
    return cnt


tt = time.time()

N = int(input())

#cnt = Ln_help(N)
cnt = Ln3_help(N)

printwrite(cnt * factorial(N-1))









fin.close()
fout.close()
del print, input

print(time.time()-tt)
