# itertools.product()

from itertools import product

s = list(map(int, input().split()))
k = list(map(int, input().split()))

w = list(product(s, k))

print(' '.join(map(str, w)))
