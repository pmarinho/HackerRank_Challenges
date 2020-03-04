# Tuples

n = int(input())

m = input().split(maxsplit=n-1)

t = ()

for i in range(n):
    aux = int(m[i])
    t = t + (aux,)

print(hash(t))
