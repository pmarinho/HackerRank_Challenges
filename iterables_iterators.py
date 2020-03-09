# Iterables and Iterators

import itertools as it

N = int(input())
letters = input().split()
K = int(input())

L = list(it.combinations(letters, K))

x = 0
y = 0
for k in L:
    if 'a' in k:
        x = x + 1

    y = y + 1

print('{0:.4f}'.format(x/y))
