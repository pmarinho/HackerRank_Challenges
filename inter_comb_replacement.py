# itertools.combinations_with_replacement()

from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)

w = list(combinations_with_replacement(s, k))

S = list()
for i in sorted(w):
    aux = "".join(sorted(i))
    S.append(aux)

for i in sorted(S):
    print(i)
