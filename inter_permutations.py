# itertools.permutations()

from itertools import permutations

s, k = input().split()
k = int(k)

perm_s = permutations(s, k)

string_perm_s = list()
for x in perm_s:
    aux = "".join(x)
    string_perm_s.append(aux)

for z in sorted(string_perm_s):
    print(z)
