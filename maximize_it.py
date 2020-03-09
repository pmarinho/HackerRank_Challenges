# Maximize It!

import itertools as it

K, M = map(int, input().split())

L = list()

for k in range(K):
    aux = list(map(int, input().split()))
    L.append(aux[1:])

C = list(it.product(*L))

C2 = list()
for i in C:
    C2.append(sum(list(map(lambda x: pow(x, 2), i)))%M)

print(max(C2))
