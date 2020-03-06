# Collections.namedtuple()

from collections import namedtuple

N = int(input())

collumns = input().split()

Students = namedtuple('Student', collumns)

sum = 0
for x in range(N):
    aux = input().split()
    for i in collumns:
        if i == 'MARKS':
            idx = collumns.index('MARKS')
            aux_2 = int(aux[idx])
            sum = sum + aux_2


avg = sum/N
print('{0:.2f}'.format(avg))
