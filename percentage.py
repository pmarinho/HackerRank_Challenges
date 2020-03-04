# Finding the percentage

import statistics

N = int(input())
names = []
grades = []
for i in range(N):
    students = input().split(maxsplit=3)
    names.append(students[0])
    aux = []
    for j in range(3):
        aux.append(float(students[j+1]))

    grades.append(aux)

name = input()

for i in names:
    if name == i:
        idx = names.index(i)
        m = statistics.mean(grades[idx])

print("{0:.2f}".format(m))
