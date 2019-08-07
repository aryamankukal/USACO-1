"""
ID: wrwwctb1
LANG: PYTHON3
TASK: pprime
1.6.3

key idea
a 10-dig num has ~10^10 possibilities, but only ~10^5 palindromes
generate palindromes and check primality

point 1/2: speed of loop

point 2/2: exploit symmetry
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

filename = 'pprime'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')







# sieve would be too slow for 1e8

def isprime(n):
    top = int(sqrt(n)) + 1
    for i in range(2, top):
        if n % i == 0:
            return False
    return True

# filter would be too slow. running through 1e8 is a problem itself

def genpalindrome_old(length):
    if length == 1:
        return [5, 6, 7, 8, 9]
    halflength = length // 2
    halflist = map(str, range(10**(halflength-1), 10**halflength))
    if length % 2 == 0:
        return [int(s+s[::-1]) for s in halflist]
    else:
        digs = list(map(str, range(10))) # digs only iter once if no list()!!
        fulllist = []
        for half in halflist:
            for d in digs:
                fulllist.append(int(half + d + half[::-1]))
        return fulllist

def genpalindrome(length):
    if length % 2 == 0:
        return geneven(length // 2)
    else:
        return genodd(-(-length >> 1))

def genodd(halflength):
    # halflength = ceil(length / 2)
    halflist = map(str, range(10**(halflength-1), 10**halflength))
    return [int(s+s[-2::-1]) for s in halflist]

def geneven(halflength):
    halflist = map(str, range(10**(halflength-1), 10**halflength))
    return [int(s+s[::-1]) for s in halflist]

a, b = map(int, input().split())

oklist = []
for length in range(1, 8+1):
    palindromelist = genpalindrome(length)
    for pal in palindromelist:
        if isprime(pal):
            oklist.append(pal)

ai = bisect_left(oklist, a)
bi = bisect_right(oklist, b)
for i in range(ai, bi):
    printwrite(oklist[i])




fin.close()
fout.close()
del print, input

