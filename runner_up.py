# Find the Runner-Up Score!

X = int(input())

A = list(map(int, input().strip().split(maxsplit=X-1)))

A.sort(reverse=True)
max_A = A[0]
A.remove(A[0])

for i in A:
    if max_A != i:
        smax_A = i
        break


print(smax_A)
