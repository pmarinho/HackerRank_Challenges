#Company Logo

alphabet = "abcdefghijklmnopqrstuvwxyz"
S = input()
S_2 = ""

for l in alphabet:
    if l in S:
        x = S.count(l)
        for i in range(x):
            S_2 = S_2 + l


# First Letter
n = []
for letter in S_2:
    n.append(S_2.count(letter))

first_letter_idx = n.index(max(n))
first_letter = S_2[first_letter_idx]
first_number = max(n)

print(first_letter + " " + str(first_number))

S_2 = S_2.replace(first_letter, "")

#Second Letter
n = []
for letter in S_2:
    n.append(S_2.count(letter))

second_letter_idx = n.index(max(n))
second_letter = S_2[second_letter_idx]
second_number = max(n)

print(second_letter + " " + str(second_number))

S_2 = S_2.replace(second_letter, "")

#Third Letter
n = []
for letter in S_2:
    n.append(S_2.count(letter))

third_letter_idx = n.index(max(n))
third_letter = S_2[third_letter_idx]
third_number = max(n)

print(third_letter + " " + str(third_number))
