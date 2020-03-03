# Lists

list_n = []

n = int(input())

for i in range(n):

    k = input().split()

    if k[0] == "print":
        print(list_n)
    elif k[0] == "sort":
        list_n.sort()
    elif k[0] == "pop":
        list_n.pop()
    elif k[0] == "reverse":
        list_n.reverse()
    elif k[0] == "append":
        list_n.append(int(k[1]))
    elif k[0] == "remove":
        list_n.remove(int(k[1]))
    elif k[0] == "insert":
        list_n.insert(int(k[1]), int(k[2]))
