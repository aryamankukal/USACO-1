"""
ID: wrwwctb1
LANG: PYTHON3
TASK: hamming
2.1.7

key idea
0 must be in the answer. if not, can create a better answer:

foo = any one codeword
for &codeword in all codewords:
    codeword ^= foo

collect all codewords that are >=D away from 0. dfs to choose N of them
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

filename = 'hamming'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')











def hamming(a, b):
    c = a ^ b
    return bin(c)[2:].count('1')

def examinePattern(B):
    dist = []
    for i in range(2**B):
        row = []
        for j in range(2**B):
            if i == j:
                row.append('*')
            else:
                if hamming(i, j) >= D:
                    row.append('*')
                else:
                    row.append(' ')

        dist.append(row)
    for i in range(2**B):
        print(''.join(dist[i]))

def check(neig, chosen, curr, D):
    for ch in chosen:
        if hamming(ch, curr) < D:
            return False
    return True

def pos2bits(neig):
    ans = 0
    for d in neig:
        ans |= 1 << d
    return ans

def dfs(neig, chosen, curr, need, D):
#    print('%2d' % len(chosen), '.'*len(chosen))
    if len(chosen) == need:
        return True

    while curr < len(neig):
        if check(neig, chosen, neig[curr], D):
            chosen.add(neig[curr])
            if dfs(neig, chosen, curr+1, need, D):
                return True
            chosen.remove(neig[curr])
        curr += 1
    return False


N, B, D = map(int, input().split())


indices = list(range(B))
neigdifpos = []
for d in range(D, B+1):
    neigdifpos.extend(list(combinations(indices, d)))

neig = [pos2bits(neig) for neig in neigdifpos] # 0 is chosen

#for n in neig:
#    print(bin(n)[2:].count('1'))
#print('')

assert len(neig) >= N - 1

chosen = set()

neig.sort()



ans = dfs(neig, chosen, 0, N-1, D)

assert ans

assert len(chosen) == N-1

out = [0]
for ch in sorted(chosen):
    out.append(ch)

# verify
for i in range(len(out)):
    for j in range(i+1, len(out)):
        assert hamming(out[i], out[j]) >= D

output = []
for i, o in enumerate(out):
    output.append(str(o))
    if i == len(out)-1:
        pass # output.append('\n')
    else:
        if i % 10 == 9:
            output.append('\n')
        else:
            output.append(' ')

printwrite(''.join(output))








fin.close()
fout.close()
del print, input

