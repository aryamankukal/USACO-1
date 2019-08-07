"""
ID: wrwwctb1
LANG: PYTHON3
TASK: cowxor
6.1.3

review

cumulative xor
put all xor vals in a trie
for each xor val:
    find in the trie its best match xor
    # best match = as inverted as possible
    ans = sequence between xor and best match

    # xor vals may appear many times
    # lastSeen dict keeps idx of those before but closest to curr xor

can save memory by differentiating leaf nodes and body nodes
turns out not required
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

filename = 'cowxor'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')













class Node:
    def __init__(self):
        self.L = None # 0
        self.R = None # 1

class Leaf(Node):
    def __init__(self):
        self.X = -1 # xor value, if leaf

def makeLeaf(curr, X, n):
    for i in range(20, -1, -1):
        mask = 1 << i
        bit = mask & X
        if bit:
            if not curr.R:
                if i > 0:
                    curr.R = Node()
                else:
                    curr.R = Leaf()
            curr = curr.R
        else:
            if not curr.L:
                if i > 0:
                    curr.L = Node()
                else:
                    curr.L = Leaf()
            curr = curr.L
    if curr.X == -1:
        curr.X = X

def findBest(X, curr):
    for i in range(20, -1, -1):
        mask = 1 << i
        bit = mask & X
        if bit:
            if curr.L:
                curr = curr.L
            else:
                curr = curr.R
        else:
            if curr.R:
                curr = curr.R
            else:
                curr = curr.L
    return curr.X

N = int(input())
root = Node()
X = 0
Xs = [X]
makeLeaf(root, X, 0)
for n in range(1, N+1):
    X ^= int(input())
    Xs.append(X)
    makeLeaf(root, X, n)


best = Xs[1]
bestIndices = 1, 1
lastSeen = {0: 0, Xs[1]:1}
for n in range(2, len(Xs)):
    Xmatch = findBest(Xs[n], root)
    if Xmatch in lastSeen: # if not, later in loop, Xmatch will find Xs[n]
        cand = Xs[n] ^ Xmatch
        if best < cand:
            best = cand
            bestIndices = lastSeen[Xmatch]+1, n
    lastSeen[Xs[n]] = n

printwrite('%d %d %d' % (best, bestIndices[0], bestIndices[1]))










fin.close()
fout.close()
del print, input

