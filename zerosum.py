"""
ID: wrwwctb1
LANG: PYTHON3
TASK: zerosum
2.3.3
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
# sys.setrecursionlimit(5782)

print = functools.partial(print, flush=True)
input = lambda: fin.readline().strip()

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'zerosum'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')








def genpatterns(n, out, curr):
    if n == 1:
        out.append(curr)
        return
    genpatterns(n-1, out, curr + [' '])
    genpatterns(n-1, out, curr + ['+'])
    genpatterns(n-1, out, curr + ['-'])


# reduce() and nextnum() can be done with eval(''.join(pattern.split()))
def nextnum(ls, pattern, i):
    '''
    return next number, taking into account spaces
    also return pos at next op
    '''
    assert i < len(ls)
    num = ls[i]
    while i < len(pattern) and pattern[i] == ' ':
        i += 1
        num = num * 10 + ls[i]
    return num, i

def reduce(ls, pattern):
    assert len(ls) == len(pattern) + 1

    op = '+'
    out = 0
    pos = 0
    while True:
        num, pos = nextnum(ls, pattern, pos)
        if op == '+':
            out += num
        elif op == '-':
            out -= num
        else:
            assert False
        if pos >= len(pattern):
            break
        op = pattern[pos]
        pos += 1
    return out

def combine(ls, pattern):
    assert len(ls) == len(pattern) + 1
    out = []
    for i in range(len(pattern)):
        out.append(str(ls[i]))
        out.append(pattern[i])
    out.append(str(ls[-1]))
    return ''.join(out)


N = int(input())

patterns = []
genpatterns(N, patterns, [])


outs = []
ls = list(range(1, N+1))
for pattern in patterns:
    if reduce(ls, pattern) == 0:
        out = combine(ls, pattern)
        outs.append(out)
#outs.sort()
for out in outs:
    printwrite(out)






fin.close()
fout.close()
del print, input

