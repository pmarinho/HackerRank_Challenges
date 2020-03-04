# Mutations

def mutate_string(string, position, character):

    string_l = list(string)

    string_l[position] = character

    string_n = "".join(string_l)

    return string_n

string = input()
pos_char = input().split()

print(mutate_string(string, int(pos_char[0]), pos_char[1]))

