"""
ID: wrwwctb1
LANG: PYTHON3
TASK: runround
2.2.5
"""

import os, sys, re, itertools, functools, heapq
from collections import Counter, deque
from copy import copy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
             sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan

print = functools.partial(print, flush=True)
input = lambda: fin.readline().strip()

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'runround'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')





def runs(strM):
    ln = len(strM)
    beenthere = [False] * ln
    curr = 0
    for _ in range(ln):
        if beenthere[curr]:
            return False
        beenthere[curr] = True
        curr = (curr + int(strM[curr])) % ln
    return curr == 0

#def onerun(strM, pos):
#    return (pos + int(strM[pos])) % len(strM)

#def allunique(strM):
#    return len(strM) == len(set([ch for ch in strM]))



M = int(input())

ln0 = floor(log10(M))+1

for ln in range(ln0, 10):

    # if length is 5, can't have 5 in the number
    if ln == 1:
        outlist = ['1','2','3','4','5','6','7','8','9']
    else:
        inlist = [1,2,3,4,5,6,7,8,9]
        outlist = []
        for i in inlist:
            if i % ln != 0:
                outlist.append(str(i))

    # use permutations because digits cannot repeat
    # note there is no sol for ln = 9, because there is not enough digits
    # no sol for ln = 8 either. not sure why
    exitflag = False
    for perm in permutations(outlist, ln):
        strnum = ''.join(perm)
        num = int(strnum)
        if num > M:
            if runs(strnum):
                printwrite(num)
                exitflag = True
                break
    if exitflag:
        break

#print(exitflag)




fin.close()
fout.close()
del print, input

