def rle(string):
    output = ''
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            output += f"{count}{string[i - 1]}"
            count = 1
    output += f"{count}{string[i - 1]}"
    return(output)

print(rle("BBBBBBBSSCCC"))