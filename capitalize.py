# Capitalize!

def solve(S):
    S_aux = ""
    cnt = 0
    Up = False
    for s in S:
        if (cnt == 0 or Up) and s != " ":
            S_aux = S_aux + s.upper()
            cnt = cnt + 1
            Up = False
        elif s == " ":
            S_aux = S_aux + s
            Up = True
            cnt = cnt + 1
        else:
            S_aux = S_aux + s
            Up = False
            cnt = cnt + 1

    return S_aux