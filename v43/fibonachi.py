fibbonachi = [1, 2] #En lista med de två första fibbonachitalen
i = 1
while fibbonachi[-1] < 4000000: #Denna loop lägger till alla fibbonachital som är mindre än 4 000 000
    fibbonachi.append(fibbonachi[i] + fibbonachi[i - 1]) #Lägger ihop de två senaste talen i listan och lägger till summan i append (slutet)
    i += 1
sum = 0
for i in fibbonachi: #Denna loop adderar summan av alla jämna fibbonachital i den tidigare skapade listan
    if i % 2 == 0: #om talet är jämnt delbart med 2...
        sum += i #...lägg till det i summan
print(sum) #Skriv ut summan