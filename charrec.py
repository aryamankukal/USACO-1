"""
ID: wrwwctb1
LANG: PYTHON3
TASK: charrec
5.4.2

key idea
k[i]   : min num of corruptions from line [0 to i]
f[i, l]: min num of corruptions from line [i to i+l), contributed by the optimally selected char

k[i] = min(k[i-19] + f[i-18, 19],
           k[i-20] + f[i-19, 20],
           k[i-21] + f[i-20, 21])


point 1/2: impression of image recognition does not apply
           NOTHING is fuzzy here
           no need for image processing or any cleanning.
           as brutal as milk4

point 2/2: bottom-up dp can have two flavors

- at curr, assume all good <  curr, look back at some curr-x, update curr
- at curr, assume all good <= curr, look ahead at some curr+x, update curr+x

the latter can be much easier to code
plus, when curr is deemed unreachable, no need to run curr at all
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

filename = 'charrec'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')














def show(image):
    for line in image:
        toShow = bin(line)[2:]
        toShow = toShow.replace('0', ' ')
        toShow = toShow.replace('1', '+')
        print(' '*(20-len(toShow)) + toShow)

def popcount(x):
    x -= (x >> 1) & 0x5555555555555555
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    return ((x * 0x0101010101010101) & 0xffffffffffffffff ) >> 56

def dp(match, accMatchF, accMatchB,
       allMinDiff, allMinDiffChi, allMinDiffHeight, row0):
    '''
    # init allMinDiff
    allMinDiff = [inf] *..
    allMinDiff[0] = 0 which is before first 19-match
    #for i in range(1, 18+1):
    #    allMinDiff[j] = inf # impossible

    row0 start at 0
    # dataImg[0] is placed for allMatchF,B
    first update is allMinDiff[0+19], first 19-match

    last row0 is such that row0 + 19 <= len(dataImg)-2

    final min mismatch is allMinDiff[-2]
    # dataImg[-1] is placed for allMatchF,B
    '''

    if allMinDiff[row0] == inf:
        return

    # best 19?
    if row0 + 19 > len(allMinDiff)-2:
        return # 19 not available

    minDiff    = inf
    minDiffChi = None

    for chi in range(27):
        col0 = 20 * chi

        currMinDiff = min(accMatchB[row0  ][col0+1 ], # skip col0
                          accMatchF[row0+1][col0+18])# skip col19
        for toSkip in range(1, 18+1):
            cand19 = accMatchB[row0  ][col0+toSkip+1] + \
                     accMatchF[row0+1][col0+toSkip-1]
            currMinDiff = min(currMinDiff, cand19)

        if currMinDiff < minDiff:
            minDiff    = currMinDiff
            minDiffChi = chi

    cand19 = minDiff + allMinDiff[row0]
    if cand19 < allMinDiff[row0+19]:
        allMinDiff      [row0+19] = cand19
        allMinDiffChi   [row0+19] = minDiffChi
        allMinDiffHeight[row0+19] = 19

    # best 20?
    if row0 + 20 > len(allMinDiff)-2:
        return # 20 not available

    minDiff    = inf
    minDiffChi = None

    for chi in range(27):
        col0 = 20 * chi
        cand20 = accMatchB[row0+1][col0]
        if cand20 < minDiff:
            minDiff = cand20
            minDiffChi = chi
    cand20 = minDiff + allMinDiff[row0]
    if cand20 < allMinDiff[row0+20]:
        allMinDiff      [row0+20] = cand20
        allMinDiffChi   [row0+20] = minDiffChi
        allMinDiffHeight[row0+20] = 20

    # best 21?
    if row0 + 21 > len(allMinDiff)-2:
        return # 21 not available

    minDiff    = inf
    minDiffChi = None

    for chi in range(27):
        col0 = 20 * chi

        currMinDiff = min(accMatchB[row0+2][col0   ], # repeat col0, row2 wins
                          accMatchF[row0+1][col0+19])# repeat col19, row20 wins
        for toRepeat in range(18+1):
            cand21 = accMatchB[row0+2][col0+toRepeat+1] + \
                     accMatchF[row0+1][col0+toRepeat  ]
            currMinDiff = min(currMinDiff, cand21)

        if currMinDiff < minDiff:
            minDiff    = currMinDiff
            minDiffChi = chi

    cand21 = minDiff + allMinDiff[row0]
    if cand21 < allMinDiff[row0+21]:
        allMinDiff      [row0+21] = cand21
        allMinDiffChi   [row0+21] = minDiffChi
        allMinDiffHeight[row0+21] = 21


# read input data image
N = int(input())
rawImg = []
for n in range(N):
    line = input()
    rawImg.append([ch for ch in line])

#clean(rawImg) # rawImg may be cleaned here. not necessary

dataImg = []
for i in range(N):
    dataImg.append(int(''.join(rawImg[i]), 2))
dataImg = [0] * 1 + dataImg + [0]

#assert False

# read font
ffont = open('font.in', 'r')
Nfont = int(ffont.readline().strip('\n'))
font2d = []
for n in range(Nfont):
    line = ffont.readline().strip('\n')
    font2d.append(int(line, 2))

#show(dataImg)
#show(font2d)

# pre calc mismatch between every pair of rows, one on dataImg, one on font2d
match = []
for dataRow in dataImg:
    matchRow = []
    for fontRow in font2d:
        # matchRow.append(bin(dataRow ^ fontRow).count('1'))
        matchRow.append(popcount(dataRow ^ fontRow)) # not much help
    match.append(matchRow)

# pre calc forward and backward diagnal accumulations of match
accMatchF = []
accMatchB = []
for i in range(len(dataImg)-19):
    rowF = []
    rowB = []
    for j in range(0, len(font2d), 20):
        F = [match[i   +k][j   +k] for k in range(20)]
        B = [match[i+19-k][j+19-k] for k in range(20)]
        accF = list(accumulate(F))
        accB = list(accumulate(B))
        rowF.extend(accF)
        rowB.extend(accB[::-1])
    accMatchF.append(rowF)
    accMatchB.append(rowB)

# dp

allMinDiff       = [inf] * len(dataImg) # min total difference (between content and best match to font) up to a row
allMinDiff[0] = 0
allMinDiffChi    = [-1] * len(dataImg) # index of char of best match at a row
allMinDiffHeight = [0] * len(dataImg) # height of the best match at a row. eveyr term is 19, 20, or 21
for row0 in range(len(dataImg)):
    dp(match, accMatchF, accMatchB,
       allMinDiff, allMinDiffChi, allMinDiffHeight, row0)

chars = ' abcdefghijklmnopqrstuvwxyz'

## debug
def toChar(i):
    if i >= 0:
        return chars[i]
    else:
        return '@'

for row in zip(range(len(allMinDiff)),
               allMinDiff,
               allMinDiffChi,
               map(toChar, allMinDiffChi),
               allMinDiffHeight):
    print(row)
#import matplotlib.pyplot as pl
#pl.plot(allMinDiff, '.')
#pl.plot([len(allMinDiff)-1]*2, [0, max(allMinDiff)])
#pl.plot([len(allMinDiff)-16]*2, [0, max(allMinDiff)])


# trace
out = []
curr = len(allMinDiffChi)-2#1#realLasti
while curr > 0: # [0] was added to dataImg #19:# > 19:
#    print(curr, chars[allMinDiffChi[curr]])
    out.append(chars[allMinDiffChi[curr]])

    if allMinDiffHeight[curr] == 0:
        #print('.', chars[allMinDiffChi[curr]], '.')
        break

    curr -= allMinDiffHeight[curr]

printwrite(''.join(out[::-1]))













fin.close()
fout.close()
del print, input

