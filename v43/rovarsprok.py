vowels = ['a', 'u', 'i', 'o', 'e', 'y', 'ö', 'å', 'ä']

def rovar_sprak(message):
    output = ''
    for char in message:
        if not(char.lower in vowels) and char.isalnum():
            output += f'{char}o{char.lower()}'
        else:
            output += char
    return(output)
            
print(rovar_sprak('Jag hatar Fabians feta jävla anus!!!'))