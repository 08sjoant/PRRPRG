string = "Packa pappas kappsäck"
p = 0
for char in string:
    if char.lower() == "p":
        p += 1
print(p)

vowels = "aeiouyåäö"
cons = 0
for char in string:
    if not(char in vowels) and char.isalnum():
        cons += 1
print(cons)

for i in range(len(string) - 1, -1, -1):
    print(string[i], end="")



for i in range(len(string) - 1, -1, -1):
    print(string[i], end="")


string = "AAAAADDDDDEEFAAAADDA"
i = 0
count = 0
temp = ""

for char in string:
    if
