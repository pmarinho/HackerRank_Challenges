# Introduction to Sets

import statistics


def average(array):

    array_s = set(array)

    avg_a = statistics.mean(array_s)

    return avg_a


a = int(input())
b = set(map(int, input().split()))

print(average(b))

