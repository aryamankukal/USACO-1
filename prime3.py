"""
ID: wrwwctb1
LANG: PYTHON3
TASK: prime3
6.4.1

review

a better search
- starts out having fewer branches every level
- starts out having fewer levels
- can be pruned eariler
- can be pruned with heavy reduction


doesn't work:
- preprocess primes. fill board digit by digit. prune
- form a primes prefix lookup tree. fill board row by row
  for every row, prune partially filled columns and diagonals


for python, details matter
- compare with .py1, list indexing matters
- at level d1 (line 180), checking triplets first matters
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

filename = 'prime3'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')











def sieve(maxNum):
    prime = [True] * (maxNum + 1)
    prime[0] = prime[1] = False
    for i in range(2, maxNum + 1):
        if prime[i]:
            for j in range(i+i, maxNum + 1, i):
                prime[j] = False
    return prime

def addDict(dc, key, digs):
    if key not in dc:
        dc[key] = []
    dc[key].append(digs)

tt = time.time()

pmax = 99999 # upper bound of primes
pmin = 10000 # lower
NDIGS = 5

prime = sieve(pmax)

totsum, start = map(int, input().split())


# good prime: digits sum to totsum. > 10000
'''
p0     > 10000     sum to totsum       can have 0
ps     > 10000     sum to totsum       no 0            start with "start"
p04    > 10000     sum to totsum       key: (0th, 4th) dig


'''

nump = 10000 # number of primes

ps = [None] * nump
nps = 0

p0set = set()

p01 = {}
p02 = {}
p03 = {}
p04 = {}
p012 = {}
p013 = {}
p014 = {}
p0123 = {}
p0124 = {}
p0134 = {}

for i in range(pmin, pmax + 1):
    if prime[i]:
        p = i

        # find sum and all digits
        ss = 0
        hasZero = False
        digs = [-1] * NDIGS
        for j in range(NDIGS):
            dig = p % 10
            if dig == 0:
                hasZero = True
            digs[NDIGS-1-j] = dig
            ss += dig
            p //= 10

        #
        if ss == totsum:
            p0set.add(tuple(digs))

            if not hasZero and digs[0] == start:
                ps[nps] = digs
                nps += 1

            addDict(p01, (digs[0], digs[1]), digs)
            addDict(p02, (digs[0], digs[2]), digs)
            addDict(p03, (digs[0], digs[3]), digs)
            addDict(p04, (digs[0], digs[4]), digs)

            addDict(p012, (digs[0], digs[1], digs[2]), digs)
            addDict(p013, (digs[0], digs[1], digs[3]), digs)
            addDict(p014, (digs[0], digs[1], digs[4]), digs)

            addDict(p0123, (digs[0], digs[1], digs[2], digs[3]), digs)
            addDict(p0124, (digs[0], digs[1], digs[2], digs[4]), digs)
            addDict(p0134, (digs[0], digs[1], digs[3], digs[4]), digs)


out = []

for r00, r01, r02, r03, r04 in ps[:nps]:
  for c00, c01, c02, c03, c04 in ps[:nps]:
    '''
    r0 r0 r0 r0 r0
    c0
    c0
    c0
    c0
    '''
    if (c04, r04) not in p04: continue

    for d00, d01, d02, d03, d04 in p04[c04, r04]:
      '''
      r0 r0 r0 r0 r0
      c0       d0
      c0    d0
      c0 d0
      c0
      '''
      if (c03, d01) not in p01: continue
      if (r03, d03) not in p01: continue
      if (c02, d02) not in p02: continue
      if (r02, d02) not in p02: continue
      if (c01, d03) not in p03: continue
      if (r01, d01) not in p03: continue
      if (r00, d02) not in p02: continue

      for d10, d11, d12, d13, d14 in p02[r00, d02]:
        '''
        r0 r0 r0 r0 r0
        c0 d1    d0
        c0    d0
        c0 d0    d1
        c0          d1
        '''
        if (c03, d01, d13) not in p013: continue
        if (r03, d03, d13) not in p013: continue
        if (c01, d11, d03) not in p013: continue
        if (r01, d11, d01) not in p013: continue
        if (c04, d14) not in p04: continue
        if (r04, d14) not in p04: continue

        for r10, r11, r12, r13, r14 in p013[c01, d11, d03]:
          '''
          r0 r0 r0 r0 r0
          c0 d1 r1 d0 r1
          c0    d0
          c0 d0    d1
          c0          d1
          '''
          if (r02, r12, d02) not in p012: continue
          if (r04, r14, d14) not in p014: continue

          for c10, c11, c12, c13, c14 in p013[r01, d11, d01]:
            '''
            r0 r0 r0 r0 r0
            c0 d1 r1 d0 r1
            c0 c1 d0
            c0 d0    d1
            c0 c1       d1
            '''
            if (c02, c12, d02) not in p012: continue
            if (c04, c14, d14) not in p014: continue

            for r20, r21, r22, r23, r24 in p012[c02, c12, d02]:
              '''
              r0 r0 r0 r0 r0
              c0 d1 r1 d0 r1
              c0 c1 d0 r2 r2
              c0 d0    d1
              c0 c1       d1
              '''
              if (r04, r14, r24, d14) not in p0124: continue
              if (r03, d03, r23, d13) not in p0123: continue

              for c20, c21, c22, c23, c24 in p0123[r03, d03, r23, d13]:
                '''
                r0 r0 r0 r0 r0
                c0 d1 r1 d0 r1
                c0 c1 d0 r2 r2
                c0 d0    d1
                c0 c1    c2 d1
                '''
                if (c04, c14, c24, d14) not in p0134: continue


                for c30, c31, c32, c33, c34 in p0124[r04, r14, r24, d14]:
                  '''
                  r0 r0 r0 r0 r0
                  c0 d1 r1 d0 r1
                  c0 c1 d0 r2 r2
                  c0 d0    d1 c3
                  c0 c1    c2 d1
                  '''
                  if (c03, d01, d13, c33) not in p0134: continue

                  for r30, r31, r32, r33, r34 in p0134[c03, d01, d13, c33]:
                    '''
                    r0 r0 r0 r0 r0
                    c0 d1 r1 d0 r1
                    c0 c1 d0 r2 r2
                    c0 d0 r3 d1 c3
                    c0 c1    c2 d1
                    '''
                    if (r02, r12, d02, r32) not in p0123: continue

                    for r40, r41, r42, r43, r44 in p0134[c04, c14, c24, d14]:
                      '''
                      r0 r0 r0 r0 r0
                      c0 d1 r1 d0 r1
                      c0 c1 d0 r2 r2
                      c0 d0 r3 d1 c3
                      c0 c1 r4 c2 d1
                      '''
                      if (r02, r12, d02, r32, r42) not in p0set: continue

                      out.append([r00, r01, r02, r03, r04,
                                  r10, r11, r12, r13, r14,
                                  r20, r21, r22, r23, r24,
                                  r30, r31, r32, r33, r34,
                                  r40, r41, r42, r43, r44])


if out:
    out.sort()

    flatout = []
    for o in out:
        flatout.extend(o)
    fout.write('\n'.join(['%d%d%d%d%d\n'*5]*len(out)) % tuple(flatout))

else:
    fout.write('NONE')









print(time.time()-tt)


fin.close()
fout.close()
del print, input

