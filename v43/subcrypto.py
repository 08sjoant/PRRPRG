import string #String används i denna kod för att skapa en sträng med alla ascii karaktärer
alphabet = string.ascii_letters #Förutnämda sträng

def encode(message, rotation): #Definerar en funkton som krypterar ett medelande (message) med 'rotation' steg.
    output = ''
    for i in message: #Vi kikar på alla bokstäver i strängen här då
        if i in alphabet: #Om symbolen finns i alfabetet (altså en bokstav)...
            for char in alphabet: #...så kollar vi vilken bokstav det råkar vara här
                if i == 'Z' and char == i:
                    output += alphabet[rotation - 1].upper()
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
        print(f"{i}. {decode(message, i)}")
    return()

# unknowndecrypt('ACOABVBCBVÄÅMJ MVÅBRMAJXR BL')

print(decode('ACOABVBCBVÄÅMJ MVÅBRMAJXR BL', 13))