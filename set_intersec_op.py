# Set .intersection() Operation

E = int(input())
E_s = set(map(int, input().split()))

F = int(input())
F_s = set(map(int,input().split()))

print(len(E_s.intersection(F_s)))

