# Nested Lists

N = int(input())

names = []
grades = []

for i in range(N):
    names.append(input())
    grades.append(float(input()))


grade_min = min(grades)
grade_min_idx = grades.index(min(grades))

grades.remove(grades[grade_min_idx])
names.remove(names[grade_min_idx])

while grade_min in grades:
    grade_min_idx = grades.index(min(grades))

    grades.remove(grades[grade_min_idx])
    names.remove(names[grade_min_idx])

idxs = [i for i, x in enumerate(grades) if x == min(grades)]

names_n = []
for i in idxs:
    names_n.append(names[i])

names_n.sort()

for i in names_n:
    print(i)
