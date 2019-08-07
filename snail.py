"""
ID: wrwwctb1
LANG: PYTHON3
TASK: snail
5.2.1

point 1/3: one idiom for steps/increments in all 4 directions
point 2/3: one idiom for both left and right turns
point 3/3: compare code volume with and without idioms above
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

filename = 'snail'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')













def sq2str(sq):
    out = []
    for row in sq:
        out.append(''.join(row))
    return '\n'.join(out)

def isOnBoard(ii, jj):
    return 0 <= ii and ii < N and 0 <= jj and jj < N

#def step(i0, j0, dr, dc): # use literal for speed
#    return i0 + dr, j0 + dc

def walk(sq, i0, j0, dr, dc):
    '''
    walk direction
    best = incremented steps

    find more directions

    for aach direction
        recurse
        update best

    unwalk

    return best seen
    '''
    # walk direction
    ii, jj = i0+dr, j0+dc
    while isOnBoard(ii, jj) and sq[ii][jj] == '.':
        sq[ii][jj] = 'o'
        ii, jj = ii+dr, jj+dc
    i1, j1 = ii-dr, jj-dc
    i2, j2 = ii, jj
    walked = abs(j1 - j0) + abs(i1 - i0)

    # find more directions and recurse
    bestFurther = 0

    if isOnBoard(i2, j2) and sq[i2][j2] == 'o':
        pass
    else:
        nr, nc = not dr, not dc
        ii, jj = i1+nr, j1+nc
        if isOnBoard(ii, jj) and sq[ii][jj] == '.':
            cand = walk(sq, i1, j1, nr, nc)
            bestFurther = max(bestFurther, cand)

        ii, jj = i1-nr, j1-nc
        if isOnBoard(ii, jj) and sq[ii][jj] == '.':
            cand = walk(sq, i1, j1, -nr, -nc)
            bestFurther = max(bestFurther, cand)

    # unwalk
    ii, jj = i1, j1
    while (ii, jj) != (i0, j0):
        sq[ii][jj] = '.'
        ii, jj = ii-dr, jj-dc

    return walked + bestFurther

def solve(sq):
    '''
    if can go east
        go east
    if can go south
        go south
    return best
    '''
    cands = []
    if sq[0][1] == '.':
        cands.append(walk(sq, 0, 0, 0, 1))
    if sq[1][0] == '.':
        cands.append(walk(sq, 0, 0, 1, 0))
    return 1 + max(cands) or 1




N, B = map(int, input().split())
sq = [['.'] * N for n in range(N)]
sq[0][0] = 'o'
for b in range(B):
    line = input()
    j = ord(line[0]) - ord('A')
    i = int(line[1:]) - 1
    sq[i][j] = '#'

ans = solve(sq)
printwrite(ans)














fin.close()
fout.close()
del print, input


















'''
"""
ID: wrwwctb1
LANG: PYTHON3
TASK: snail
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

filename = 'snail'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')














def sq2str(sq):
    out = []
    for row in sq:
        out.append(''.join(row))
    return '\n'.join(out)

def walk(sq, i0, j0, dr):
#
#    walk direction
#    best = incremented steps
#
#    find more directions
#
#    for aach direction
#        recurse
#        update best
#
#    unwalk
#
#    return best seen
#
    # walk direction
    if dr == 'E':
        jj = j0 + 1
        while jj < N and sq[i0][jj] == '.':
            sq[i0][jj] = 'o'
            jj += 1
        i1 = i0
        j1 = jj - 1
        walked = j1 - j0
    elif dr == 'W':
        jj = j0 - 1
        while 0 <= jj and sq[i0][jj] == '.':
            sq[i0][jj] = 'o'
            jj -= 1
        i1 = i0
        j1 = jj + 1
        walked = j0 - j1
    elif dr == 'N':
        ii = i0 - 1
        while 0 <= ii and sq[ii][j0] == '.':
            sq[ii][j0] = 'o'
            ii -= 1
        i1 = ii + 1
        j1 = j0
        walked = i0 - i1
    elif dr == 'S':
        ii = i0 + 1
        while ii < N and sq[ii][j0] == '.':
            sq[ii][j0] = 'o'
            ii += 1
        i1 = ii - 1
        j1 = j0
        walked = i1 - i0

    # find more directions
    moreDrs = []
    if dr == 'E':
        if jj < N and sq[i0][jj] == 'o':
            pass
        else:
            if 1 <= i0   and sq[i0-1][j1] == '.':
                moreDrs.append('N')
            if i0 <= N-2 and sq[i0+1][j1] == '.':
                moreDrs.append('S')
    elif dr == 'W':
        if 0 <= jj and sq[i0][jj] == 'o':
            pass
        else:
            if 1 <= i0   and sq[i0-1][j1] == '.':
                moreDrs.append('N')
            if i0 <= N-2 and sq[i0+1][j1] == '.':
                moreDrs.append('S')
    elif dr == 'N':
        if 0 <= ii and sq[ii][j0] == 'o':
            pass
        else:
            if 1 <= j0   and sq[i1][j0-1] == '.':
                moreDrs.append('W')
            if j0 <= N-2 and sq[i1][j0+1] == '.':
                moreDrs.append('E')
    elif dr == 'S':
        if ii < N and sq[ii][j0] == 'o':
            pass
        else:
            if 1 <= j0   and sq[i1][j0-1] == '.':
                moreDrs.append('W')
            if j0 <= N-2 and sq[i1][j0+1] == '.':
                moreDrs.append('E')

    # recurse
    bestFurther = 0
    for md in moreDrs:
        cand = walk(sq, i1, j1, md)
        bestFurther = max(bestFurther, cand)

    # unwalk
    if dr == 'E':
        for jj in range(j0+1, j1+1):
            sq[i0][jj] = '.'
    elif dr == 'W':
        for jj in range(j0-1, j1-1, -1):
            sq[i0][jj] = '.'
    elif dr == 'N':
        for ii in range(i0-1, i1-1, -1):
            sq[ii][j0] = '.'
    elif dr == 'S':
        for ii in range(i0+1, i1+1):
            sq[ii][j0] = '.'


    return walked + bestFurther

def solve(sq):
#
#    if can go east
#        go east
#    if can go south
#        go south
#    return best
#
    cands = []
    if sq[0][1] == '.':
        cands.append(walk(sq, 0, 0, 'E'))
    if sq[1][0] == '.':
        cands.append(walk(sq, 0, 0, 'S'))
    return 1 + max(cands) or 1




N, B = map(int, input().split())
sq = [['.'] * N for n in range(N)]
sq[0][0] = 'o'
for b in range(B):
    line = input()
    j = ord(line[0]) - ord('A')
    i = int(line[1:]) - 1
    sq[i][j] = '#'

ans = solve(sq)
printwrite(ans)














fin.close()
fout.close()
del print, input


'''
