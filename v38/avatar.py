'''Skriv ett program som genom en meny ger en avatar tre egenskaper plus ett namn:

    Namn, ska kunna sättas till godtycklig sträng
    Färg, ska kunna väljas gul (g), blå (b) eller röd (r)
    Styrka, ska kunna väljas som ett heltal mellan 1 och 10
    Pronomen, ska kunna väljas han, hon eller hen
    Menyn ska vara inmatningssäker, dvs om användaren anger ett otillåtet värde så ska denna inmatning (och enbart denna inmatning) göras om.
'''
#Exempelkörning:
'''
Ange avatarens namn -> Efelia
Ange färgen för Efelia: Gul (g), Blå (b) eller Röd (r) -> s
Otillåtet val! Ange färgen Gul (g), Blå (b) eller Röd (r) -> r
Ange styrka (heltal 1 - 10) -> 7
Ange tilltalspronomen (han/hon/hen) -> hon

# Datorn skriver ut
Det här är Efelia, hon är en röd avatar med styrkan 7.
Snabbheten beräknas till 3.
'''

import random

i = 1

name = input('Ange avatarens namn >')
while i > 0:
    color = input('Ange färgen för ' + name + ': grön, blå eller röd >')
    if color != 'röd' and color != 'grön' and color != 'blå':
        print('Otillåtet val! Ange färgen [g]ul, [b]lå eller [r]öd')
    else:
        break
while i > 0:
    strength = input('Ange styrka (heltal 1 - 10) >')
    strength = int(strength)
    if not 1 <= strength <= 10:
        print('Ogiltit tal')
    else:
        break
strength = str(strength)
while i > 0:
    pronoun = input('Ange tilltalspronomen (han/hon/hen) >')
    if pronoun != 'han' and pronoun != 'hon' and pronoun != 'hen':
        print('Stava rätt nu! >:(')
    else:
        break

print('Det här är ' + name + ', ' + pronoun + ' är en ' + color + ' avatar med styrkan ' + strength)