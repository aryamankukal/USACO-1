"""
ID: wrwwctb1
LANG: PYTHON3
TASK: fence8
6.3.1

review
classic
dfs bisect id
prune at 4 places
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
sys.setrecursionlimit(5782)
# python -m cProfile -s time ha.py

print = functools_partial(print, flush=True)
input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'fence8'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









def tryk(rails, cutBoards, maxWasteMid, iRail, iBoard):
    '''
    rails        sorted list, never change
    cutBoards    list, will update
    maxWasteMid  int, never change
    iRail        idx from R-1 downwards. ie consider large rails first
    iBoard       idx from 0 upwards. ie consider boards in one order (no sort)

    top call:    tryk(rails, cutBoards, maxWasteMid,
                      largest rails index to consider,
                      0)
    '''
    if iRail < 0:
        return True

    # prune 3: check wasted boards
    waste = 0
    for board in cutBoards:
        if board < rails[0]:
            waste += board
    if maxWasteMid < waste:
        return False

    # if the rail at hand is the same as the prev, don't look back
    # otherwise, do look back
    # iBoard != 0 is rquired,
    # such that we don't consider beyond the largest rails index intended
    currRail = rails[iRail]
    if iBoard != 0 and currRail != rails[iRail+1]:
        iBoard = 0

    for jBoard in range(iBoard, len(cutBoards)):

        # if current rail can fit a board, try it
        if currRail < cutBoards[jBoard]:

            cutBoards[jBoard] -= currRail
            if tryk(rails, cutBoards, maxWasteMid, iRail - 1, jBoard):
                return True
            cutBoards[jBoard] += currRail

        # prune 4
        # if current rail fit a board perfectly, sol exsits iff this try works
        elif currRail == cutBoards[jBoard]:

            cutBoards[jBoard] = 0
            if tryk(rails, cutBoards, maxWasteMid, iRail - 1, jBoard + 1):
                return True
            cutBoards[jBoard] = currRail
            return False

    return False



N = int(input())
boards = []
for n in range(N):
    boards.append(int(input()))

R = int(input())
rails = []
for r in range(R):
    rails.append(int(input()))
rails.sort()

# prune 1: remove largest rails if sumRails > sumBoaards
sumRails = sum(rails)
sumBoards = sum(boards)
while sumRails > sumBoards:
    sumRails -= rails[-1]
    del rails[-1]
R = len(rails)

# for rails[0]~rails[i], how much baord can be wasted?
accRails = list(accumulate(rails))
maxWaste = [sumBoards - waste for waste in accRails]

# prune 2: is there a solution
solExists = False
for board in boards:
    if board >= rails[0]:
        solExists = True
        break

if not solExists:
    printwrite(0)
else:
    # bisect for solution. invariant: left <= sol <= right
    left = 0
    right = R - 1
    while left < right:
        mid = -(-(left + right) // 2) # round up
        cutBoards = copy(boards)
        check = tryk(rails, cutBoards, maxWaste[mid], mid, 0)
        if check:
            left = mid
        else:
            right = mid - 1
    printwrite(right + 1)







fin.close()
fout.close()
del print, input

