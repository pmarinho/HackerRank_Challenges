# Compress the String!

from itertools import groupby

S = input()

G = list()

for key, grp in groupby(S):
    G.append('({}, {})'.format(len(list(grp)), key))

print(*G)
