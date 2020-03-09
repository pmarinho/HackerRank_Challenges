# The Captain's Room

K = int(input())
rooms = list(map(int, input().split()))

rooms_set = set(rooms)

print(int((K * sum(rooms_set) - sum(rooms)) / (K - 1)))
