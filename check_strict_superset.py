# Check Strict Superset

A = set(map(int, input().split()))

T = int(input())

for t in range(T):
    B = set(map(int, input().split()))

    if A.issuperset(B) and A != B:
        state = True
    else:
        state = False
        break

print(state)