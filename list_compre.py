# List Comprehensions

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())
list_N = []

for i in range(X+1):
    for j in range(Y+1):
        for k in range(Z+1):

            if i+j+k != N:
                vec = [i, j, k]
                list_N.append(vec)

print(list_N)
