# Print Function

def print_n(n):

    y = 0
    if n <= 9:
        for i in range(n):
            x = (i+1)*pow(10, n-i-1)
            y = y + x
    else:
        for i in range(9):
            x = (i+1)*pow(10, 9-i-1)
            y = y + x
        for j in range(10, n+1):
            ct = 0
            w = j
            while w > 0:
                w = w//10
                ct = ct + 1
            y = y*pow(10, ct) + j

    print(y)


z = int(input())

print_n(z)
