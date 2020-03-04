# Designer Door Mat

import math

N, M = map(int, input().split())

k = math.floor(N/2)

c = ".|."
d = "-"
w = round((M-7)/2)

#Top Cone
for i in range(k):
    print((d*round((M-3*(2*i+1))/2)).rjust(k-i)+c*(2*i+1)+(d*round((M-3*(2*i+1))/2)).ljust(k-i))

print((d*w).rjust(k-1)+"WELCOME"+(d*w).ljust(k-1))

for i in range(k):
    print((d*round(3*(i+1))).rjust(i)+c*(N-2*i-2)+(d*round(3*(i+1))).ljust(i))
