def rle(string):
    output = ''
    count = 0
    for i in range (1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            output += f"{count}{string[i - 1]}"
            count = 1
        output += f"{count}{string[-1]}"
    return(output)

print(rle('BBBBSSCCC'))

def numbers_between(tal1, tal2):
    if tal1 < tal2:
        for i in range(tal1 + 1, tal2):
            print(i)
    elif tal2 < tal1:
        for i in range(tal2 + 1, tal1):
            print(i)
    return()

numbers_between(1, 12)
