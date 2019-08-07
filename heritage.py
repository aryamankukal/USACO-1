"""
ID: wrwwctb1
LANG: PYTHON3
TASK: heritage
3.4.2
"""

import os, sys, re
from collections import Counter, deque, defaultdict
from copy import copy
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

filename = 'heritage'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')












def gen1(inn, pre, post):
    # this takes lots of memeory 39819104
    n = len(inn)
    assert n == len(pre) == len(post)
    if n == 0:
        return
    root = pre[0]
    post[-1] = root
    innrootidx = inn.find(root)

    gen1(inn[:innrootidx], pre[1:1+innrootidx], post[n-innrootidx-1:-1]) # left tree

    gen1(inn[innrootidx+1:], pre[1+innrootidx:], post[:n-innrootidx-1]) # right tree

def gen2(ini, inj, pri, prj, poi, poj):
    n = inj - ini
    assert n == prj - pri == poj - poi
    if n == 0:
        return
    root = pre[pri]
    post[poj-1] = root
    innrootidx = inn.find(root, ini, inj)
    lenl = innrootidx - ini
    lenr = inj - innrootidx - 1

    gen2(ini, ini+lenl, pri+1, pri+1+lenl, poi, poi+lenl) # left tree

    gen2(inj-lenr, inj, prj-lenr, prj, poj-1-lenr, poj-1) # right tree




inn = input()
pre = input()
n = len(inn)
assert n == len(pre)
post = [''] * n

gen2(0, n, 0, n, 0, n)

printwrite(''.join(post))













fin.close()
fout.close()
del print, input

