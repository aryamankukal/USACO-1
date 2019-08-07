"""
ID: wrwwctb1
LANG: PYTHON3
TASK: transform
1.3.3
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

filename = 'transform'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')





def transpose(mat):
    return list(zip(*mat))

def reflect(mat):
    newmat = []
    for row in mat:
        newmat.append(row[::-1])
    return newmat

def rotate90(mat):
    return reflect(transpose(mat))

def rotate180(mat):
    return rotate90(rotate90(mat))

def rotate270(mat):
    return rotate90(rotate180(mat))

N = int(input())

mat1 = []
for n in range(N):
    row = input()
    mat1.append(tuple(re.findall('.',row)))

mat2 = []
for n in range(N):
    row = input()
    mat2.append(tuple(re.findall('.',row)))

if mat2 == rotate90(mat1):
    ans = 1
elif mat2 == rotate180(mat1):
    ans = 2
elif mat2 == rotate270(mat1):
    ans = 3
else:
    ref1 = reflect(mat1)
    if mat2 == ref1:
        ans = 4
    elif mat2 == rotate90(ref1) or \
         mat2 == rotate180(ref1) or \
         mat2 == rotate270(ref1):
        ans = 5
    elif mat2 == mat1:
        ans = 6
    else:
        ans = 7

printwrite(ans)

fin.close()
fout.close()
del print, input

