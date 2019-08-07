"""
ID: wrwwctb1
LANG: PYTHON3
TASK: betsy
6.5.3

was betsy22.py
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
#input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'betsy'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')
ttt = time.time()














Nmax = 7
Nmax2 = 49
N = 0
N2 = 0





def dfs(Nfilled, i, j):
    # i, j is the last filled loc
    if i == N and j == 1:
        if Nfilled == N2:
            return 1
        else:
            return 0

    # neighbors of i j are the only ones whose acc changed in the previous call
    ijneigs = []

    for x in [i-1, i+1]:
        if x < 1 or N < x or board[x][j]:
            continue
        ijneigs.append((x, j))

    for y in [j-1, j+1]:
        if y < 1 or N < y or board[i][y]:
            continue
        ijneigs.append((i, y))

    for x, y in ijneigs:
        if acc[x][y] == 0: # isolated
            if not (x == N and y == 1 and Nfilled == N2 - 1):
                return 0

    # body choke type 1: when i j does a cut, return 0
    '''
    s x x x x x
    x x . . . x
    x x . . . x
    . . x . . x
    . . x . . x
    t . x x x x
    '''
    if len(ijneigs) == 3 and 1 <= i and i <= N and 1 <= j and j <= N:
        if   board[i + 1][j] and (board[i - 1][j - 1] or board[i - 1][j + 1]):
            return 0
        elif board[i - 1][j] and (board[i + 1][j - 1] or board[i + 1][j + 1]):
            return 0
        elif board[i][j - 1] and (board[i - 1][j + 1] or board[i + 1][j + 1]):
            return 0
        elif board[i][j + 1] and (board[i - 1][j - 1] or board[i + 1][j - 1]):
            return 0

    # body choke type 2: when i j does a cut, return 0
    '''
    s x x x x x
    . . x . . x
    . . x . . x
    . . x . . x
    . . x . . x
    t . x x x x
    '''
    if len(ijneigs) == 2:
        n1, n2 = ijneigs
        n1x, n1y = n1
        n2x, n2y = n2
        if n1x == n2x or n1y == n2y:
            return 0

    # one-entrance
    for x, y in ijneigs:
        if acc[x][y] == 1 and not (x == N and y == 1):
            ijneigs = [(x, y)]
            break

    # wall bottleneck: when about to hit a wall: aim away from target
    '''
    s x x . .
    . . x . .
    . . x x .
    . . . . .
    t . . . .
    '''
    if len(ijneigs) == 3:
        if   i == 2     and board[3    ][j    ]: # top
            ijneigs = [(2    , j - 1)]
            if debugFlag:
                P(2    , j - 1)
                input()
            assert not board[2    ][j - 1]

        elif i == N - 1 and board[N - 2][j    ]: # bot
            ijneigs = [(N - 1, j + 1)]
            if debugFlag:
                P(N - 1, j + 1)
                input()
            assert not board[N - 1][j + 1]

        elif j == 2     and board[i    ][3    ]: # left
            ijneigs = [(i - 1, 2    )]
            if debugFlag:
                P(i - 1, 2    )
                input()
            assert not board[i - 1][2    ]

        elif j == N - 1 and board[i    ][N - 2]: # right
            ijneigs = [(i - 1, N - 1)]
            if debugFlag:
                P(i - 1, N - 1)
                input()
            assert not board[i - 1][N - 1]

    '''
    how to steer body bottleneck like wall bottleneck?

    s . . . . .
    x . x x . .
    x . . x . .    not necessarily toward or away from target
    x . . x . .
    x x x x . .
    t . . . . .

    s x x x x x
    x x . . . x
    x x . . . x
    x x . x x x
    x x . . . .
    t . . . . .

    s x x x x x x
    x x x x x x x
    . . . . . . x    toward path's mass center? incorrect
    . x x x x . x
    . x . . . . x
    . x . . . . x
    t x x x x x x

    toward inside the path? 2 vers, both slow

    s x . . . . .
    x x . x x x .
    x . . . . x .
    x . . . . x .
    x . . . . x .
    x x x x x x .
    t . . . . . .

    v1: keep updating a path polygon cumulative area. check sign of area. N^2

    path:
        1  2  3  4
        x1 x2 x3 x4
        y1 y2 y3 y4
    path polygon cumulative area (2x) (tail open):
        1 ?
        2 x1y2-y1x2
        3 x1y2-y1x2 + x2y3-y2x3
        4 x1y2-y1x2 + x2y3-y2x3 + x3y4-y3x4
    wanted path area is a suffix
    sign of area determines "inside"

    fun: area and path length yield num of enclosed lattice points (pick's th)


    v2: toward the larger path num in front

    difficult to identify "front" so might need O(N). too slow

    1  6  7 10 11 12
    2  5  8  9 14 13
    3  4  .  . 15 16
    .  .  .  .  . 17
    .  * 23  .  . 18
    .  . 22 21 20 19

    1 12 13 18 19 22 23
    2 11 14 17 20 21 24
    3 10 15 16  .  . 25
    4  9  .  *  .  . 26
    5  8  . 34 33 32 27
    6  7  .  .  . 31 28
    .  .  .  .  . 30 29

    '''

    cnt = 0
    for x, y in ijneigs:
        if (x < 1 or N < x or y < 1 or N < y or board[x][y]):
            continue

        xyneigs = []
        for u in [x-1, x+1]:
            if 1 <= u and u <= N:
                xyneigs.append((u, y))
        for v in [y-1, y+1]:
            if 1 <= v and v <= N:
                xyneigs.append((x, v))

        board[x][y] = Nfilled + 1
        for u, v in xyneigs:
            acc[u][v] -= 1

        cnt += dfs(Nfilled + 1, x, y)


        board[x][y] = 0
        for u, v in xyneigs:
            acc[u][v] += 1
    return cnt

def dfs_help():
    if N == 1:
        return 1
    elif N == 2:
        return 1

    for i in range(2, N):
        for j in range(2, N):
            acc[i][j] = 4
    for i in range(2, N):
        acc[1][i] = acc[i][1] = acc[N][i] = acc[i][N] = 3
    acc[1][1] = acc[N][1] = acc[1][N] = acc[N][N] = 2

    acc[1][2] -= 1
    acc[2][1] -= 1

    board[1][1] = 1

    return dfs(1, 1, 1)

def debugPrint(var, ni=None, nj=None):

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if var[i][j]:
                print('%3d' % var[i][j], end='')
            else:
                if i == ni and j == nj:
                    print('  *', end='')
                else:
                    print('  .', end='')
        print('')
    print('')

def P(ni=None, nj=None):
    debugPrint(board, ni, nj)

def A():
    debugPrint(acc)

N = 7 # int(fin.readline().strip('\n'))
N2 = N * N

board = [[0] * (Nmax + 1) for n in range(Nmax + 1)]

acc = [[0] * (Nmax + 1) for n in range(Nmax + 1)] # accessibility

debugFlag = False

testCnt = 0

ans = dfs_help()

printwrite(ans)








fin.close()
fout.close()
del print #, input
print(time.time() - ttt)
