# Symmetric Difference

M = int(input())
M_l = set(map(int, input().split()))

N = int(input())
N_l = set(map(int, input().split()))

x = M_l.difference(N_l)
y = N_l.difference(M_l)

z = x | y

for i in sorted(z):
    print(i)
