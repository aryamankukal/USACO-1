"""
ID: wrwwctb1
LANG: PYTHON3
TASK: milk4
5.3.2

key idea
unbounded knapsack with tricky solution selection

so far the most brutal

point 1/2:
each s[q] only depends on itself and s[q-pail[i]]
it's a lot more subtle to trace the required optimal set
see note

point 2/2:
drastic speed difference (>>10) between milk4.cpp and milk4.py for milk46.in
milk4.py and milk4.cpp use exact same algo. only latter can pass
milk4.py1 uses search and dp. a c++ translation would've passed
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

filename = 'milk4'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')










def show():
#    ' '.join(['%4s'] * (Q+1)) % tuple(map(str, s))
    print('   q    s    l   n')
    for q in range(Q+1):
        print('%4s %4s %4s %4s' % \
              (str(q), str(s[q]), str(l[q]), str(n[q])))
    print('pails', pail)

def track(qa, qb, l, n):
    if qa == qb:
        return False
    while qa and qb:
        if l[qa] < l[qb]:
            return True
        elif l[qa] > l[qb]:
            return False
        else:
            qa -= n[qa] * l[qa]
            qb -= n[qb] * l[qb]
    if qa == 0:
        return False
    else:
        return True

Q = int(input())
P = int(input())
pail = []
for p in range(P):
    pail.append(int(input()))

pail = [None] + sorted(set(pail), reverse=True)


s = [inf] * (Q + 1) # s[q] = size of min set pail for q
l = [0]   * (Q + 1) # l[q] = last pail used
n = [0]   * (Q + 1) # n[q] = num of times last pail used

s[0] = 0 # no pail is needed for q==0

for i in range(1, len(pail)): # run through pails
    paili = pail[i]

    ts = copy(s)
    tl = copy(l)
    tn = copy(n)

    for q in range(1, Q+1):
        if q >= paili:
            prevq = q - paili

            if ts[prevq] < inf: # prevq reachable from top
                if tl[prevq] == paili:
                    ts[q] = ts[prevq]
                    tl[q] = paili
                    tn[q] = tn[prevq] + 1
                else:
                    ts[q] = ts[prevq] + 1
                    tl[q] = paili
                    tn[q] = 1

                if s[prevq] < inf: # prevq reachable from left

                    # is left better?
                    if (s[prevq] + 1 < ts[q] or # strictly better
                        (s[prevq] + 1 == ts[q] and # tie
                         track(prevq, q - tn[q] * paili, l, n))):
                         # ^ compare two branches:
                         # (1) prevq reached from left, paili not included
                         # (2) topmost entry in column i, paili not included

                        ts[q] = s[prevq] + 1
                        tl[q] = paili
                        tn[q] = 1

    # is q reachable from left? is it better? update s l n
    for q in range(1, Q+1):
        if ts[q] <= s[q]:
            s[q] = ts[q]
            l[q] = tl[q]
            n[q] = tn[q]
#    show()

q = Q
traced = []
while q > 0:
    print(q, l[q], n[q])
    traced.append(l[q])
    q -= l[q] * n[q]

printwrite(' '.join(['%d'] * (s[-1] + 1)) % tuple([s[-1]] + traced))

fin.close()
fout.close()
del print, input

