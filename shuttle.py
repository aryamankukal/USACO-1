"""
ID: wrwwctb1
LANG: PYTHON3
TASK: shuttle
4.4.1

key idea
all answers have the same length so dfs suffices
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

filename = 'shuttle'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')












def can(state, i):
    if state[i] == 0:
        if i+1 < NN and state[i+1] == None:
            return '0move'
        if i+2 < NN and state[i+2] == None:
            return '0jump'
    if state[i] == 1:
        if i-1 >= 0 and state[i-1] == None:
            return '1move'
        if i-2 >= 0 and state[i-2] == None:
            return '1jump'
    return None

def forward(state, i, moveJump):
    if moveJump == '0move':
        state[i] = None
        state[i+1] = 0
        return
    if moveJump == '0jump':
        state[i] = None
        state[i+2] = 0
        return
    if moveJump == '1move':
        state[i] = None
        state[i-1] = 1
        return
    if moveJump == '1jump':
        state[i] = None
        state[i-2] = 1
        return

def backward(state, i, moveJump):
    if moveJump == '0move':
        state[i] = 0
        state[i+1] = None
        return
    if moveJump == '0jump':
        state[i] = 0
        state[i+2] = None
        return
    if moveJump == '1move':
        state[i] = 1
        state[i-1] = None
        return
    if moveJump == '1jump':
        state[i] = 1
        state[i-2] = None
        return

def dfs(state, choices):
    if state == final:
        return True
    for i in range(NN):
        moveJump = can(state, i)
        if moveJump:
            choices.append(i)
            forward(state, i, moveJump)
            if dfs(state, choices):
                return True
            del choices[-1]
            backward(state, i, moveJump)
    return False


tt = time.time()

# constants
N = int(input())
NN = 2 * N + 1
final = [1] * N + [None] + [0] * N

# search. it seems there are only two solutions of equal lengths
state = [0] * N + [None] + [1] * N
choices = []
dfs(state, choices)

# output
choices = [c+1 for c in choices]

out = []
i = 0
while i < len(choices):
    out.append(' '.join(map(str, choices[i:i+20])))
    i += 20
out = '\n'.join(out)
printwrite(out)

print(time.time()-tt)








fin.close()
fout.close()
del print, input

