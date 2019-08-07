"""
ID: wrwwctb1
LANG: PYTHON3
TASK: clocks
6.5.4

review

constant time sol exists

num of all distinct combinations of moves = 4**9 (order doesn't matter)


my sol doesn't use the above

num of all distinct states = 4**9

states, moves and state transitions are coded in bits
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

filename = 'clocks'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









def clocks2bits(clocks):
    num = 0
    for i in range(len(clocks)):
        num += (clocks[i] // 3 % 4) * (1 << (i << 1))
    return num

def moveLet2bits(moveLet):
    move = 0
    for ch in moveLet:
        d = ord(ch) - ord('A')
        move += 1 << 2*d
    return move

def transition(clocks, move):
    b0 = clocks & 0b010101010101010101
    b1 = clocks & 0b101010101010101010
    a0 = b0 ^ move
    a1 = b1 ^ ((b0 & move) << 1)
    return a0 + a1


clocks = []
for i in range(3):
    row = list(map(int, input().split()))
    clocks.extend(row)
clocks = clocks2bits(clocks)

moveLets = ['ABDE',
            'ABC',
            'BCEF',
            'ADG',
            'BDEFH',
            'CFI',
            'DEGH',
            'GHI',
            'EFHI']

moves = []
for moveLet in moveLets:
    moves.append(moveLet2bits(moveLet))

#tests = [3, 4, 7, 8]
##tests = [4, 7, 3, 8]
#print(bin(clocks))
#for test in tests:
#    clocks = transition(clocks, moves[test])
#    print(bin(clocks))

seen = [False] * (4**9)
seen[clocks] = True
qq = deque()
qq.append(clocks)

parent = [-1] * (4**9)
arrivedVia = [-1] * (4**9)

# bfs
while qq:
    u = qq.popleft()
    if u == 0: # destination
        break
    for i, move in enumerate(moves):
        v = transition(u, move)
        if seen[v]:
            continue
        seen[v] = True
        qq.append(v)
        parent[v] = u
        arrivedVia[v] = i

# trace
v = 0
used = []
while True:
    u = parent[v]
    if u == -1:
        break
    used.append(arrivedVia[v] + 1)
    v = u

printwrite(' '.join(['%d'] * len(used)) % tuple(used[::-1]))












fin.close()
fout.close()
del print, input

