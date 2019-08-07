"""
ID: wrwwctb1
LANG: PYTHON3
TASK: twofive
5.5.3

key idea
dp
see comments below
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

filename = 'twofive'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')












def numWays(coor):
    '''
    return num of possible full boards,
    given coor of ch that are already placed

    code sections where comments are applicable are marked

    comment 1:
    aa bb cc dd ee are num of ch on the 1st 2nd 3rd 4th 5th row

    comment 2:
    if nothing is on the board, this is beautiful dp
    if we fill the board by the alphabetical order,
    every possible placement of ch must have a left and a top neighbor
    so that board is valid

    but time and again, ordering solutions using dp info can be tricky

    consider the 10000th board, ABCDEFGHIKJMNQRLOTVXPSUWY

    in the wrong version (commented out below), at this board
    --
    A B C D E
    F G H I K
    J M N *
    L O #

    --
    ch == P but * needs to be Q
    the num of skipped boards is nw[5][5][4][2][0] == 162
    so later P is put at #

    in the correct version,  when the board progresses to
    --
    A B C D E
    F G H I K
    J M N *
    --
    * needs to be Q. the num of skipped boards for *==P is 246,
    which is the sum of these two boards' num of ways in the wrong version

    --nw[5][5][4][2][0]==162
    A B C D E
    F G H I K
    J M N P
    L O
    --nw[5][5][4][1][1]==84
    A B C D E
    F G H I K
    J M N P
    L
    O
    --

    comment 3:
    now ch has a fixed loc,
    at the present board situation, where ch is to be placed,
    the required loc may or may not be reachable
    only when it is reachable, and only the value (nw) of the reached board
    should be copied to the present board


    things can be much neater if python supported references
    rowFill = [5, 0, 0, 0, 0, 0]
    for rowFill[1] in ...:
        for rowFill[2] in ...:
            ...
                ch = sum(rowFill[1:])
                target = & nw[rowFill[1]][rowFill[2]][rowFill[3]][rowFill[4]][rowFill[5]]

                if coor[ch] == [-1, -1]:
                    for row in range(1, 6):
                        if rowFill[row] < rowFill[row-1]:
                            rowFill[row] += 1
                            target = nw[rowFill[1]][rowFill[2]][rowFill[3]][rowFill[4]][rowFill[5]]
                            rowFill[row] -= 1
                else:
                    row, col = coor[ch]
                    if rowFill[row] < rowFIll[row-1] and rowFill[row] + 1 == col:
                        rowFill[row] += 1
                        target = nw[rowFill[1]][rowFill[2]][rowFill[3]][rowFill[4]][rowFill[5]]
                        rowFill[row] -= 1


    '''

    # nw = number of possible full boards, if starting from
    # aa, bb, cc, dd, ee chars **fixed** in the 1st, the 2nd,..., the 5th row
    nw = [[[[[0] * 6
             for bb in range(6)]
            for cc in range(6)]
           for dd in range(6)]
          for ee in range(6)]
    nw[5][5][5][5][5] = 1

    # comment 1

    for aa in range(5, 0, -1):
        for bb in range(aa, -1, -1):
            for cc in range(bb, -1, -1):
                for dd in range(cc, -1, -1):
                    for ee in range(dd, -1, -1):
                        # ch = char to place
                        ch = aa + bb + cc + dd + ee # 1=B
                        if coor[ch] == [-1, -1]:

                            # comment 2

                            if aa < 5:
                                nw[aa][bb][cc][dd][ee] += nw[aa+1][bb][cc][dd][ee]
                            if bb < aa:
                                nw[aa][bb][cc][dd][ee] += nw[aa][bb+1][cc][dd][ee]
                            if cc < bb:
                                nw[aa][bb][cc][dd][ee] += nw[aa][bb][cc+1][dd][ee]
                            if dd < cc:
                                nw[aa][bb][cc][dd][ee] += nw[aa][bb][cc][dd+1][ee]
                            if ee < dd:
                                nw[aa][bb][cc][dd][ee] += nw[aa][bb][cc][dd][ee+1]
                        else:

                            # comment 3

                            row, col = coor[ch]
                            if row == 1 and aa < 5  and aa + 1 == col:
                                nw[aa][bb][cc][dd][ee] = nw[aa+1][bb][cc][dd][ee]
                            if row == 2 and bb < aa and bb + 1 == col:
                                nw[aa][bb][cc][dd][ee] = nw[aa][bb+1][cc][dd][ee]
                            if row == 3 and cc < bb and cc + 1 == col:
                                nw[aa][bb][cc][dd][ee] = nw[aa][bb][cc+1][dd][ee]
                            if row == 4 and dd < cc and dd + 1 == col:
                                nw[aa][bb][cc][dd][ee] = nw[aa][bb][cc][dd+1][ee]
                            if row == 5 and ee < dd and ee + 1 == col:
                                nw[aa][bb][cc][dd][ee] = nw[aa][bb][cc][dd][ee+1]


    return nw[1][0][0][0][0]

NorW = input()
if NorW == 'N':
    num = int(input())
    board = [[' '] * 6 for i in range(6)]
    coor = [[-1, -1] for ch in range(26)] # -1, -1 if ch has not been placed
    for i in range(1, 6):
        for j in range(1, 6):
            for ch in range(25):
                if coor[ch] != [-1, -1]: # placed already
                    continue
                coor[ch] = [i, j]
                nw = numWays(coor)
                if nw >= num:
                    # num can be covered by nw
                    # so keep ch on i, j
                    board[i][j] = chr(ord('A') + ch)
                    break
                else:
                    # nw cannot cover num
                    # ch cannot be i, j. its associated ways must be skipped
                    num -= nw
                    coor[ch] = [-1, -1]
    # flatten board
    out = board[1][1:] + board[2][1:] + board[3][1:] + board[4][1:] + board[5][1:]
    printwrite(''.join(out))

else:
    way = input()
    board = [' ' * 6,
             ' ' + way[  : 5],
             ' ' + way[ 5:10],
             ' ' + way[10:15],
             ' ' + way[15:20],
             ' ' + way[20:25]]
    num = 0
    coor = [[-1, -1] for ch in range(26)] # -1, -1 if ch is not yet seen
    for i in range(1, 6):
        for j in range(1, 6):
            for ch in range(25):
                if coor[ch] != [-1, -1]: # seen already
                    continue
                if board[i][j] == chr(ord('A') + ch):
                    # if ch is the wanted choice, good
                    coor[ch] = [i, j] # meaning ch is seen
                    break # not skipping any more ways
                else:
                    # if ch is not the wanted one,
                    # the ways associated with it must be skipped
                    coor[ch] = [i, j]
                    num += numWays(coor)
                    coor[ch] = [-1, -1]
    printwrite(num + 1)














fin.close()
fout.close()
del print, input

