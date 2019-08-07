"""
ID: wrwwctb1
LANG: PYTHON3
TASK: milk3
1.5.3

key idea
dfs on all states. memo visited states
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

filename = 'milk3'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')







def traverse(state, seen, good, cap):
    # check state
    if state in seen:
        return
    seen.add(state)

    if checkstate(state):
        good.add(state[2])

    # try all possible transition
    for s, t in [[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]]:
        newstate = transition(state, s, t, cap)
        traverse(newstate, seen, good, cap)

def transition(state, s, t, cap):
    tspace = cap[t] - state[t]
    tomove = min(tspace, state[s])
    newstate = list(state)
    newstate[t] += tomove
    newstate[s] -= tomove
    return tuple(newstate)

def checkstate(state):
    if state[0] == 0:
        return True
    else:
        return False


cap = list(map(int, input().split()))
seen = set()
good = set()
state = (0, 0, cap[2])

#state = transition(state, 2, 0, cap)
traverse(state, seen, good, cap)

good = sorted(good)
#printwrite('%d '*len(good) % tuple(good)) # trailing space is not ok
printwrite(' '.join(['%d']*len(good)) % tuple(good))




fin.close()
fout.close()
del print, input

