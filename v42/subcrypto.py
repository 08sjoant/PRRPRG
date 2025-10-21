import string
alphabet = string.ascii_letters

def encode(message, rotation):
    output = ''
    for i in message:
        if i in alphabet:
            for char in alphabet:
                if i == 'Z' and char == i:
                    output += 'C'
                elif char == i:
                    if char.isupper():
                        output += alphabet[alphabet.index(char) + rotation].upper()
                    else:
                        output += alphabet[alphabet.index(char) + rotation].lower()
        else:
            output += i
    return(output)

print(encode('ZooKeepersTycoonBallsOfSteelISAccc', 3))

def decode(message, rotation):
    output = ''
    for i in message:
        if i in alphabet:
            for char in alphabet:
                if char == i:
                    if char.isupper():
                        output += alphabet[alphabet.index(char) - rotation].upper()
                    else:
                        output += alphabet[alphabet.index(char) - rotation].lower()
        else:
            output += i
    return(output)

print(decode('CrrNhhshuvWbfrrqEdoovRiVwhhoLVDfff', 3))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ. "

def unknowndecrypt(message):
    for i in range(len(message)):
        print(decode(message, i))
    return()

unknowndecrypt('ACOABVBCBVÄÅMJ MVÅBRMAJXR BL')