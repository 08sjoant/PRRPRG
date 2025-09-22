#uppgift 2
sum = 0

lst = list(range(1, 101))
for i in lst:
    sum = sum + i

print(sum)

#uppgift 3
from random import randint

slumplista = []
jämn = []
udda = []
for i in range(11):
    slumplista.append(randint(1,100))
for item in slumplista:
    if slumplista(item) % 2 == 0:
        jämn.append(slumplista[item])
    else:
        udda.append(slumplista[item])

print(jämn)
print(udda)