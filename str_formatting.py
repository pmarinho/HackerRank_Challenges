# String Formatting

def print_formatted(N):
    N_bin = bin(N).replace("0b", "")

    for n in range(1, N + 1):
        n_bin = bin(n).replace("0b", "")
        n_hex = hex(n).replace("0x", "")
        n_oct = oct(n).replace("0o", "")

        if n_hex.islower():
            n_hex = n_hex.upper()

        print(str(n).rjust(len(N_bin)) + str(n_oct).rjust(len(N_bin) + 1) + str(n_hex).rjust(len(N_bin) + 1) + str(
            n_bin).rjust(len(N_bin) + 1))


print_formatted(int(input()))

