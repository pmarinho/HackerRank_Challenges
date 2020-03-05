# collections.Counter()

N = int(input())

Sizes = list(map(int, input().split()))

C = int(input())

aux = 0
for i in range(C):
    c, v = map(int, input().split())

    if c in Sizes:
        aux = aux + v
        Sizes.remove(c)


print(aux)
