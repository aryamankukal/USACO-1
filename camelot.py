"""
ID: wrwwctb1
LANG: PYTHON3
TASK: camelot
3.3.4

point 1/2: interesting to think about

for each square r c,
    calculate the shortest paths for all knights to reach r c
    every knight can take many possible shortest paths. mark all the routes
    ans[r][c]=
        sum of each knight's shortest path length to r c
        +
        king's shortest shortest path length to marked routes

then pick best ans among r c

ans[r][c] is not the fastest way for r c, but the best ans among r c is correct
consider a 2 x 26 board:

king                      knight
                     rc

ans_true[r][c] (<= ans[r][c]) involes knight going past rc to fetch king
but min(ans_true) == min(ans)
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

filename = 'camelot'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')











def Ato1(ch):
    return ord(ch)-64

def bfs(board, R, C, r, c):
    oldlayer = [(r, c)]
    layernum = 0
    deli = [2, 1, -1, -2, -2, -1, 1, 2]
    delj = [-1, -2, -2, -1, 1, 2, 2, 1]
    while len(oldlayer) > 0:
        newlayer = []
        layernum += 1
        for i, j in oldlayer:
            for d in range(8):
                curri = i + deli[d]
                currj = j + delj[d]
                if 1 <= curri and curri <= R and \
                   1 <= currj and currj <= C and \
                   board[curri][currj] == -1:
                    board[curri][currj] = layernum
                    newlayer.append((curri, currj))
        oldlayer = newlayer

def avalanche(mark, board, currlayer, knightr, knightc):
    if mark[knightr][knightc]:
        return

    mark[knightr][knightc] = 1

    delr = [2, 1, -1, -2, -2, -1, 1, 2]
    delc = [-1, -2, -2, -1, 1, 2, 2, 1]
    for d in range(8):
        currr = knightr + delr[d]
        currc = knightc + delc[d]
        if 1 <= currr and currr <= R and \
           1 <= currc and currc <= C and \
           not mark[currr][currc] and \
           board[currr][currc] == currlayer - 1:
            avalanche(mark, board, currlayer-1, currr, currc)

def kingbfs(mark, kingr, kingc):
    deli = [1, 0, -1, -1, -1, 0, 1, 1]
    delj = [-1, -1, -1, 0, 1, 1, 1, 0]
    oldlayer = [(kingr, kingc)]
    state = [[0] * (C+1) for _ in range(R+1)] # 0 fresh 1 in queue 2 done
    layernum = 0
    while len(oldlayer) > 0:
        newlayer = []
        for i, j in oldlayer:
            if mark[i][j] == 1:
                return layernum
            state[i][j] = 2
            for d in range(8):
                curri = i + deli[d]
                currj = j + delj[d]
                if 1 <= curri and curri <= R and \
                   1 <= currj and currj <= C and \
                   mark[curri][currj] != -1 and \
                   state[curri][currj] == 0:
                    newlayer.append((curri, currj))
                    state[curri][currj] = 1
                    '''
                    point 2/2: need 3 states here
                    st neighbors of i j don't add one another in queue
                    '''

        oldlayer = newlayer
        layernum += 1
    return inf

R, C = map(int, input().split())
line = input().split()
king = int(line[1]), Ato1(line[0])
knights = []
while True:
    line = input()
    if line == '':
        break
    line = line.split()
    for i in range(0, len(line), 2):
        knights.append((int(line[i+1]), Ato1(line[i])))

best = inf
board = [[-1] * (C+1) for r in range(R+1)]
mark = [[0] * (C+1) for _ in range(R+1)]
for r in range(1, R+1):
    for c in range(1, C+1):
        # r, c is target loc

        # bfs, get layers, from r, c
        for i in range(R+1):
            for j in range(C+1):
                board[i][j] = -1
        board[r][c] = 0
        bfs(board, R, C, r, c)

        # sometimes a knight cannot reach r, c
        canreach = True
        for knightr, knightc in knights:
            if board[knightr][knightc] == -1:
                canreach = False
                break
        if not canreach:
            continue

        # avalanche mark every knight's every possible shortest path to r, c
        for i in range(R+1):
            for j in range(C+1):
                mark[i][j] = 0
        mark[r][c] = 1
        for knightr, knightc in knights:
            avalanche(mark, board, board[knightr][knightc], knightr, knightc)

        # king's shortest path to avalanche marks
        cand = kingbfs(mark, *king)

        # cand = all knights' shortest path len + above king's path len
        for knightr, knightc in knights:
            cand += board[knightr][knightc]

        if cand < best:
            best = cand

printwrite(best)









fin.close()
fout.close()
del print, input

