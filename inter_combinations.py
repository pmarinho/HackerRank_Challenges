# itertools.combinations()

from itertools import combinations

s, k = input().split()
k = int(k)

for j in range(1, k+1):
    w = list(combinations(s, j))

    S = list()
    for i in sorted(w):
        aux = "".join(sorted(i))
        S.append(aux)

    for i in sorted(S):
        print(i)
