"""
ID: wrwwctb1
LANG: PYTHON3
TASK: lgame
4.3.4

key idea
generate permutations of given letters. see if the generated is/are words

checking pairs from dict is too slow
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

filename = 'lgame'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')







def checkComplexity():
    '''
    has redundancy: pr m    m pr
    not considered: word len >= 3
    '''

    n = 7
    total = 0
    for k in range(1, n+1):
        temp = cnk(n, k) * (k * factorial(k))
        print(temp)
        total += temp
    print(total)


def cnk(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))



def scoref(word):
    tot = 0
    perchar = [2,5,4,4,1,6,5,5,1,7,6,3,5,2,3,5,7,2,1,2,4,6,6,7,5,7]
    for ch in word:
        tot += perchar[ord(ch) - 97] # a=97
    return tot


tt = time.time()

# read dict
din = open('lgame.dict', 'r')
words = set()
while True:
    line = din.readline().strip('\n')
    if line == '.':
        break
    words.add(line)
words.add('') # [' ', 'prm'] counts as 'prm'



chs = input()
chs = [ch for ch in chs]
n = len(chs)

#tot = 0

best = 0
book = set()
for k in range(3, n + 1): # k: total num of letters used
    for perm in permutations(chs, k): # all permutations using k letters

        for sep in [0] + list(range(3, k - 2)):
            # for sep==0, word1=='', word2== whole

#            tot += 1

            word1 = ''.join(perm[:sep])
            word2 = ''.join(perm[sep:])

            if word1 not in words or word2 not in words:
                continue

            score = scoref(word1) + scoref(word2)

            if score >= best:
                if word1 < word2:
                    if word1 == '':
                        word = word2
                    else:
                        word = ' '.join([word1, word2])
                else:
                    word = ' '.join([word2, word1])
                if score > best:
                    best = score
                    book.clear()
                    book.add(word)
                elif score == best:
                    book.add(word)


book = sorted(book)

printwrite(best)
for word in book:
    printwrite(word)



#print(time.time()-tt)


fin.close()
fout.close()
del print, input

