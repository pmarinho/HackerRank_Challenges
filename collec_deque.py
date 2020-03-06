# Collections.deque()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()
N = int(input())

for i in range(N):

    aux = input().split()

    if aux[0] == 'pop':
        d.pop()
    if aux[0] == 'append':
        d.append(str(aux[1]))
    if aux[0] == 'appendleft':
        d.appendleft(str(aux[1]))
    if aux[0] == 'popleft':
        d.popleft()

print(*d)
