# Exceptions

N = int(input())
A = list()
B = list()

for i in range(N):
    a,b = input().split()

    A.append(a)
    B.append(b)

for i in range(N):

    try:
        print(int(A[i])//int(B[i]))
    except ZeroDivisionError as ze:
        print("Error Code: " + str(ze))
    except ValueError as ve:
        print("Error Code: " + str(ve))
