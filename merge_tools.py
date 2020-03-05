# Merge the Tools!

import textwrap

def merge_the_tools(string, k):

    string_k = textwrap.wrap(string, k)
    string_k_new = list()

    for i in range(len(string_k)):
        aux = ""
        for j in string_k[i]:
            if j not in aux:
                aux = aux + j

        string_k_new.append(aux)

    for x in string_k_new:
        print(x)

