# Check Subset

T = int(input())

state = list()

for t in range(T):
    nA = int(input())
    A = set(map(int, input().split()))
    nB = int(input())
    B = set(map(int, input().split()))

    if A.issubset(B):
        state.append(True)
    else:
            state.append(False)

for st in state:
    print(st)
