"""
ID: wrwwctb1
LANG: PYTHON3
TASK: cryptcow
6.3.2

review
search with pruning
most critical:
any substring between any of {C, O, W} must be an original unaltered substring

interesting speed trade off

test data:
BeCOgC CC execuOf DOBCiCCrWaOOt theCOCeak oWWin Oon aWtheOOW EscapeWtWWWwn


file       main feature                              performance
.py        set()                                      6s
.py1       elf hash wo collision handling            17s
.cpp1      char *, unordered_set                      6s
.cpp       string, elf hash wo collision handling     2s
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

filename = 'cryptcow'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')











def checkLetterCounts(target, given):
    lenTarget = len(target)
    lenGiven = len(given)
    if lenGiven < lenTarget:
        return False
    delta = lenGiven - lenTarget
    mult, rem = divmod(delta, 3)
    if rem != 0:
        return False
    cntTarget = Counter(target)
    cntGiven = Counter(given)

    if delta > 0:
        cntTarget['C'] = mult
        cntTarget['O'] = mult
        cntTarget['W'] = mult

    if cntTarget != cntGiven:
        return False
    return True

def recurse(target, given, subs, seen):
    tl = len(target)
    gl = len(given)
    if tl == gl:
        return target == given

    # compare before first C and after last W
    # this covers cases where first ind is not C or last ind is not W
    C0 = given.index('C')
    W1 = given.rindex('W')
    targetSubStart = tl-(gl-W1)+1
    if targetSubStart < 0 or tl < targetSubStart:
        return False
    if target[:C0] != given[:C0]:
        return False
    if target[targetSubStart:] != given[W1+1:]:
        return False

    trimmedTarget = target[C0:tl-(gl-W1)+1]

    # find all C O W
    # check all sub strings between each C O W
    Cs = []
    Os = []
    Ws = []
    prev = -1
    for i, ch in enumerate(given):
        if ch == 'C' or ch == 'O' or ch == 'W':
            if ch == 'C':
                Cs.append(i)
            elif ch == 'O':
                Os.append(i)
            else:
                Ws.append(i)

            # substrings between any C W O need to be in target
            if given[prev+1:i] not in subs:
                return False
            prev = i

    # generate possible rewinds, recurse
    for O in Os:
        for C in Cs:
            for W in Ws:
                if C < O and O < W:
                    cand = (given[C0:C]  +
                            given[O+1:W] +
                            given[C+1:O] +
                            given[W+1:W1+1])
                    if cand not in seen:
                        seen.add(cand)
                        if recurse(trimmedTarget, cand, subs, seen):
                            return True
    return False






tt = time.time()

target = 'Begin the Escape execution at the Break of Dawn'
given = input()


if not checkLetterCounts(target, given):
    printwrite('%d %d' % (0, 0))
else:
    # find set of substrings
    subs = set([''])
    for i in range(len(target)):
        for j in range(i+1, len(target)+1):
            subs.add(target[i:j])

    seen = set()
    if recurse(target, given, subs, seen):
        printwrite('%d %d' % (1, (len(given)-len(target))//3))
    else:
        printwrite('%d %d' % (0, 0))

print(time.time()-tt)









fin.close()
fout.close()
del print, input

