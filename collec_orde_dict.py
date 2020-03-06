# Collections.OrderedDict()

from _collections import OrderedDict

OD = OrderedDict()

N = int(input())

for i in range(N):
    item_price = input().split()
    item = ''
    price = ''
    for j in item_price:
        if j.isalpha():
            item = item + j + ' '
        else:
            price = price + j

    price = int(price)
    item = item[:-1]

    if item in OD:
        OD[item] = OD[item] + price
    else:
        OD[item] = price

for i,j in OD.items():
    print(i, j)
