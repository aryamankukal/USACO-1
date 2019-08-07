"""
ID: wrwwctb1
LANG: PYTHON3
TASK: preface
2.2.3
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

filename = 'preface'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')






def roman(n):
    thou, n = divmod(n, 1000)
    hund, n = divmod(n, 100)
    tens, ones = divmod(n, 10)
    out = []
    if thou == 0:
        pass
    else: # thou <= 3 is givien
        out.append('M'*thou)

    if hund == 0:
        pass
    elif hund <= 3:
        out.append('C'*hund)
    elif hund == 4:
        out.append('CD')
    elif hund <= 8:
        out.append('D'+'C'*(hund-5))
    else: # hund == 9
        out.append('CM')

    if tens == 0:
        pass
    elif tens <= 3:
        out.append('X'*tens)
    elif tens == 4:
        out.append('XL')
    elif tens <= 8:
        out.append('L'+'X'*(tens-5))
    else: # tens == 9
        out.append('XC')

    if ones == 0:
        pass
    elif ones <= 3:
        out.append('I'*ones)
    elif ones == 4:
        out.append('IV')
    elif ones <= 8:
        out.append('V'+'I'*(ones-5))
    else: # ones == 9
        out.append('IX')
    out = ''.join(out)
    cnt = Counter()
    for ch in out:
        cnt[ch] += 1
    return cnt

N = int(input())

#for n in [1,5,10,50,100,500,1000,
#          3,300,268,4,9,40,39,
#          490,99,990,90]:
#    print(n, roman(n))

cnt = Counter()

# give keys an order
cnt['I'] = 0
cnt['V'] = 0
cnt['X'] = 0
cnt['L'] = 0
cnt['C'] = 0
cnt['D'] = 0
cnt['M'] = 0

for n in range(1, N+1):
    cnt += roman(n)

for key in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
    if cnt[key] != 0:
        printwrite('%s %d' % (key, cnt[key]))





fin.close()
fout.close()
del print, input

