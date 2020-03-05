#The Minion Game

vowels = "AEIOU"


def minion_game(string):
    stuart = 0
    kevin = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevin = kevin + len(string) - i
        else:
            stuart = stuart + len(string) - i

    if stuart > kevin:
        print("Stuart " + str(stuart))
    elif stuart < kevin:
        print("Kevin " + str(kevin))
    else:
        print("Draw")


print(minion_game(input()))
