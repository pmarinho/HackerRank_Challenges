# sWAP cASE

def swap_case(String):
    new_string = ""

    for i in String:
        if i.islower():
            new_string = new_string + i.upper()
        elif i.isupper():
            new_string = new_string + i.lower()
        else:
            new_string = new_string + i

    return new_string

