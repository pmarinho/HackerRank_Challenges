# Set .discard(), .remove() & .pop()

N = int(input())
S = set(map(int, input().split()))
C = int(input())

for i in range(C):
    aux = input().split()

    if aux[0] == 'pop':
        S.pop()
    elif aux[0] == 'remove':
        S.remove(int(aux[1]))
    elif aux[0] == 'discard':
        S.discard(int(aux[1]))

print(sum(S))
