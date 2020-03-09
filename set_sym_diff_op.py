# Set .symmetric_difference() Operation

E = int(input())
E_s = set(map(int, input().split()))

F = int(input())
F_s = set(map(int,input().split()))

print(len(E_s.symmetric_difference(F_s)))

