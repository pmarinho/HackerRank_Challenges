# Find a string

def count_substring(string, sub_string):
    cnt = 0
    for i in range(len(string)):
        idx = string.find(sub_string, i)

        if i == idx:
            cnt = cnt + 1

    return cnt