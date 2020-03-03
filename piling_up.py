#Piling Up!

import math

T = int(input())
N = []
sL_M = []
CB = []

for t in range(T):

    n = int(input())
    N.append(n)

    sL = list(map(int, input().split()))

    sL_M.append(sL)


for t in range(T):

    cb = True
    sL = sL_M[t]
    n = N[t]

    n_min_idx = sL.index(min(sL))

    for i in range(n_min_idx, n-1):
        if sL[i] <= sL[i+1]:
            cb = True
        else:
            cb = False
            break

    for j in range(n_min_idx):
        if sL[j] >= sL[j+1]:
            cb = True
        else:
            cb = False
            break


    CB.append(cb)

for i in range(len(CB)):

    if CB[i] == True:
        print("Yes")
    else:
        print("No")
