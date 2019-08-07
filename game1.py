"""
ID: wrwwctb1
LANG: PYTHON3
TASK: game1
3.3.6

key idea
game and dp
consider dij: delta score that the starter can achieve, given a[i]...a[j]
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

filename = 'game1'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')














@lru_cache(maxsize=None)
def D(i, j):
    '''
    D: delta scores that the starter can achieve, given a[i]...a[j]
    return results for choosing left and choosing right
    '''
    if i == j:
        return a[i], a[i]
    return a[i] - max(D(i+1, j)), a[j] - max(D(i, j-1))


N = int(input())
a = []
while True:
    line = input()
    if line == '':
        break
    a.extend(map(int, line.split()))


#D(0, len(a)-1)

# sim, or equivalently, tracing dp results
i = 0
j = len(a) - 1
A = 0 # player 1 score
B = 0
turn = True # True: 1's turn. False: 2's turn
while i <= j:
    left, right =  D(i, j)
    if left >= right:
        if turn:
            A += a[i]
        else:
            B += a[i]
        i += 1
    else:
        if turn:
            A += a[j]
        else:
            B += a[j]
        j -= 1
    turn = not turn
printwrite('%d %d' % (A, B))












fin.close()
fout.close()
del print, input

