# Time Delta

from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):

    format = '%a %d %b %Y %H:%M:%S %z'

    dt1 = dt.strptime(t1, format)
    dt2 = dt.strptime(t2, format)

    delta = (dt1 - dt2).total_seconds()

    return abs(int(delta))


t = int(input())
x = list()
for t_itr in range(t):
    t1 = input()

    t2 = input()

    delta = time_delta(t1, t2)

    x.append(delta)

for i in x:
    print(i)
