import time
import random

def slow(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

i = 1

while i <= 12:
    print(i, '* 12 =', i * 12)
    i = i + 1

i = 1
lottorad = [random.randint(1, 35)]

while i <= 6:
    slumptal = random.randint(1, 35)
    for item in lottorad:
        if slumptal not in lottorad:
            lottorad.append(slumptal)
            i = i + 1

print(lottorad)

i = 1
svarsalt = ['1', 'X', '2']
lottorad = []

while i <=13:
    slumptal = random.randint(0, 2)
    lottorad.append(svarsalt[slumptal])
    i = i + 1

print(lottorad)

i = 1
answer = random.randint(1, 10)
guess = 0

while i >= 1:
    guess = input('Gissa ett heltal mellan 1 och 10 >')
    num = int(guess)
    if num == answer:
        break
    elif num <= answer:
        print('Talet ', guess, ' är för litet' )
        i = i + 1
    elif num >= answer:
        print('Talet ', guess, ' är för stort' )
        i = i + 1

print('RÄTT GISSAT!')
print('Du klarade spelet på gissning nr. ', i, '.')

i = 1
x = -50

print('2x + 3y = 120:')

while x <= 50:
    y = -50
    while y <= 50:
        if 2*x + 3*y == 120:
            print(f"En lösning: (x, y) = ({x}, {y}) ")
        y = y + 1 #67
    x = x + 1
# wow kolla, 69 rader kod