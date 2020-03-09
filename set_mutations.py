# Set Mutations

A = int(input())
A_s = set(map(int, input().split()))

N = int(input())

for i in range(N):
    i_com = input().split()
    i_set = set(map(int,input().split()))

    if i_com[0] == 'intersection_update':
        A_s.intersection_update(i_set)
    if i_com[0] == 'update':
        A_s.update(i_set)
    if i_com[0] == 'symmetric_difference_update':
        A_s.symmetric_difference_update(i_set)
    if i_com[0] == 'difference_update':
        A_s.difference_update(i_set)

print(sum(A_s))

