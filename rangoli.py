# Alphabet Rangoli

import string

def print_rangoli(N):

    n2l_dict = dict(enumerate(string.ascii_lowercase))

    M = int(4*N-3)
    d = "-"
    w = round((M-7)/2)
    L = list()

    for i in range(N):
        aux1 = ""
        aux2 = n2l_dict[N - 1 - i]
        aux3 = ""

        if i == 0:
            aux_res = n2l_dict[N-1-i]
        elif i == 1:
            aux1 = n2l_dict[N - i] + d
            aux2 = n2l_dict[N - 1 - i]
            aux3 = d + n2l_dict[N - i]

            aux_res = aux1 + aux2 + aux3
        else:
            for k in range(i):
                aux1 = aux1 + n2l_dict[N - 1 - k] + d
                aux3 = aux3 + d + n2l_dict[N - i + k]


            aux_res = aux1 + aux2 + aux3

        L.append((d*round((M-2*(2*i+1))/2)).rjust(N-i-1) + aux_res + (d*round((M-2*(2*i+1))/2)).ljust(N-i-1))
        print((d*round((M-2*(2*i+1))/2)).rjust(N-i-1) + aux_res + (d*round((M-2*(2*i+1))/2)).ljust(N-i-1))

    for l in reversed(L):
        if l != L[-1]:
            print(l)


print_rangoli(int(input()))