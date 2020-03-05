# DefaultDict Tutorial


N, M = map(int, input().split())

A = list()
B = list()

for i in range(N):
    A.append(input())

for i in range(M):
    B.append(input())

for i in B:
    if i in A:
        indices = [j+1 for j, x in enumerate(A) if x == i]
        print(*indices)
    else:
        print(-1)
