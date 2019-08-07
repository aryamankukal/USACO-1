"""
ID: wrwwctb1
LANG: PYTHON3
TASK: hidden
5.5.2

key idea

cyclic => concat 2 copies

prerequisite:
one (not the best) way to test if two strings are cyclic shifts of each other
ref: https://jim-think.blogspot.com/2012/07/usaco-hidden-password.html
implementation: isCyclicShifts2
explanation:
suppose s1 and s2 are cyclic shifts of each other. suppose sm is the min cyclic
shift of both. suppose M(s1) is the min start loc of sm in s1. M(s2) defined
similarly. i/j points at s1/s2. maintain invariant: i <= M(s1) and j <= M(s2).
at some i j, we find the first k >= 0 s.t s1[i+k] != s2[j+k]. if s1 and s2
remains the same even if k reaches L, we found the cyclic match. otherwise,
suppose s2[j+k] > s1[i+k]. this guarantees that M(s2) cannot be in [j, j+k].
this allows us to advance j by k + 1.

back to usaco hidden:
concat input by itself. compare it with itself using the algo above, but never
allows i == j (or else we simply find that the string matches itself.) once i
or j lands on M(s), the other will be pushed to L or beyond.






n^2 methods:
    brute force: concat. strncmp L. can pass with c
    ring linked list, compare every shift (constant shift, linear compare)
    stock span, weed out suboptimal (consider 'ab'* 50000)

usaco linear sol is complicated
s = original str
ss = original str concat 2 copies
v[i] = k:
    for all substrings ss[i:i+length],
    k is the longest length s.t. ss[i:i+k] is the smallest among all ss's substrings of length k
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

filename = 'hidden'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')







'''
def isCyclicShifts2(s1, s2):
    L = len(s1)
    if len(s2) != L:
        return False
    if L == 0:
        return True
    s1 = s1 + s1
    s2 = s2 + s2
    i = 0
    j = 0
    while i < L and j < L:
        # find first difference
        k = 0
        while k < L and s1[i + k] == s2[j + k]: # i + k, j + k always < 2L
            k += 1
        # found the cyclic match
        if k == L:
            return True
        # advance
        if s1[i + k] < s2[j + k]:
            j += k + 1
        else:
            i += k + 1
    return False

def isCyclicShifts1(s1, s2):
    L = len(s1)
    if len(s2) != L:
        return False
    s2 = s2 + s2
    return s2.find(s1) != -1
'''

L = int(input())
chs = []
while True:
    line = input()
    if line == '':
        break
    chs.extend([ch for ch in line])

chs = ''.join(chs + chs)

i = 0
j = 1
while i < L and j < L:
    # find first difference
    k = 0
    while k < L and chs[i + k] == chs[j + k]: # i + k, j + k always < 2L
        k += 1
    # iff chs is uniform
    if k == L:
        break
    # advance
    if chs[i + k] < chs[j + k]:
        j += k + 1
    else:
        i += k + 1
    # never start at same place
    if i == j:
        j += 1

printwrite(min(i, j))
















fin.close()
fout.close()
del print, input

