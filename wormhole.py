"""
ID: wrwwctb1
LANG: PYTHON3
TASK: wormhole
1.4.7

interesting

nested algos:
    generation of all pairings (suitable for interviews)
    cycle detection

key idea
recursion for pairings generation. at each level:
    find the *first* unpaired (ie i)
    try pairing i with each unpaired that *follows* i (ie j)
    there is one i but many j
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

filename = 'wormhole'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









def checkcycle(pair, pt, right, N):
    # check all points
    for i in range(1, N+1):
        # start walking from i
        start = i

        # walk n steps
        for n in range(N):
            start = right[pair[start]]

        # not cycle, will reach some point that has no right neighbor
        if start != 0:
            return True
    return False


def checkallpairs(pair, pt, right, N):

    # the greedy part. only need to take first i
    i = 1
    while True:
        if i > N:
            break
        if pair[i] == None:
            break
        i += 1

    # base case when all paired
    if i > N:
        if checkcycle(pair, pt, right, N):
            return 1
        else:
            return 0


    tot = 0

    # backtrack. i can be paired to many js
    for j in range(i+1, N+1):
        if pair[j] == None:
            pair[i] = j
            pair[j] = i
            tot += checkallpairs(pair, pt, right, N)
            pair[i] = None
            pair[j] = None
    return tot

N = int(input())
pt = [None] # 1-based
for n in range(1, N+1):
    pt.append(list(map(int, input().split())))


# right neighbor. 0 if none
right = [0] * (N+1)
for i in range(1, N+1):
    for j in range(1, N+1):
        if pt[i][1] == pt[j][1] and \
           pt[i][0] < pt[j][0]:
            if right[i] == 0 or (pt[j][0] < pt[right[i]][0]):
                right[i] = j


pair = [None] * (N+1)
pair[0] = 0

tot = checkallpairs(pair, pt, right, N)

printwrite(tot)


fin.close()
fout.close()
del print, input

