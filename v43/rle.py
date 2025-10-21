def rle(string):
    output = ''
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]: #kollar om bokstav i är samma sak som den innan i strängen
            count += 1 #om den är det lägger den till 1 i count
        elif count > 1: #om symbolerna inte är samma och count har räknat upp minst en gång...
            output += f"{count}{string[i - 1]}" #...lägger den till count och bokstaven i i output
            count = 1 #count börjar om
        else:
            output += string[i - 1] #om count är 1, ska ettan inte skrivas ut; följande kod exekveras
    if string[-1] != string[-2]: #edgecase för om sista bokstaven är ensamstånde...
        output += string[-1]
    else:
        output += f"{count}{string[i - 1]}" #...arnars läggs sista sekvensen av "siffra + bokstav" till i output
    return(output)

print(rle("BBKBBBBBBSSCCCCD"))