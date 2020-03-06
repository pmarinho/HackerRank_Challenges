# No Idea!

n, m = map(int, input().split())


a = input().split()

A = set(input().split())
B = set(input().split())

cnt = 0
for i in a:
    cnt = cnt + (i in A) - (i in B)

print(cnt)
