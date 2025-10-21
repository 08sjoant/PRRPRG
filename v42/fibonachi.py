fibbonachi = [1, 2]
i = 1
while fibbonachi[-1] < 4000000:
    fibbonachi.append(fibbonachi[i] + fibbonachi[i - 1])
    i += 1
sum = 0
for i in fibbonachi:
    if i % 2 == 0:
        sum += i
print(sum)