"""
ID: wrwwctb1
LANG: PYTHON3
TASK: wissqu
6.4.3
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

filename = 'wissqu'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')








def isBadPos(i, j, ch):
    if board[i  ][j  ] == ch: return True
    if board[i-1][j-1] == ch: return True
    if board[i+1][j+1] == ch: return True
    if board[i-1][j+1] == ch: return True
    if board[i+1][j-1] == ch: return True
    if board[i-1][j  ] == ch: return True
    if board[i+1][j  ] == ch: return True
    if board[i  ][j-1] == ch: return True
    if board[i  ][j+1] == ch: return True
    return False

def recurse(step):
    if step == 17:
        global cnt
        cnt += 1
        global foundFlag
        if not foundFlag:
            for i in range(1, 17):
                printwrite('%s %d %d' % (' ABCDE'[hch[i]], hi[i], hj[i]))
            foundFlag = True
#        P()
        return

    for ch in range(1, 6):
        if not toPut[ch]:
            continue

        for i in range(1, 5):
            for j in range(1, 5):
                if done[i][j] or isBadPos(i, j, ch):
                    continue

                if not foundFlag:
                    hch[step] = ch
                    hi[step] = i
                    hj[step] = j

                boardijold = board[i][j]
                board[i][j] = ch
                done[i][j] = 1
                toPut[ch] -= 1

                recurse(step + 1)

                board[i][j] = boardijold
                done[i][j] = 0
                toPut[ch] += 1

def P():
    print(cnt)
    for row in board:
        print(row)
    print('')
    for row in done:
        print(row)
    print('')
    print(toPut)


tt = time.time()

board = [[0] * 6]
for i in range(4):
    line = [0]
    line.extend([ord(ch)-64 for ch in input()])
    line.append(0)
    board.append(line)
board.append([0] * 6)

done = [[0] * 6 for i in range(6)]
cnt = 0
toPut = [0, 3, 3, 3, 4, 3]
hch = [0] * 17 # h for history
hch[1] = 4
hi = [0] * 17
hj = [0] * 17
foundFlag = False

for i in range(1, 5):
    for j in range(1, 5):
        if isBadPos(i, j, 4):
            continue

        if not foundFlag:
            hi[1] = i
            hj[1] = j

        boardijold = board[i][j]
        board[i][j] = 4
        done[i][j] = 1
        toPut[4] -= 1

        recurse(2)

        board[i][j] = boardijold
        done[i][j] = 0
        toPut[4] += 1

printwrite(cnt)










fin.close()
fout.close()
del print, input

print(time.time()-tt)
