"""
ID: wrwwctb1
LANG: PYTHON3
TASK: ride
1.2.2
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

filename = 'ride'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')





def char2num(ch):
    return ord(ch) - 64 # ord('A')

def str2num(st):
    num1 = 1
    for ch in st:
        num1 *= char2num(ch)
    return num1

num1 = str2num(input())
num2 = str2num(input())

if num1 % 47 == num2 % 47:
    printwrite('GO')
else:
    printwrite('STAY')




fin.close()
fout.close()
del print, input

