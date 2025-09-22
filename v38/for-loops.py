import random

for i in range(9):
    print(i * '* ')

print('')

for i in range(8):
    print((8-i) * '* ')

for i in range(9):
    print(i * '* ')
for i in range(8):
    print((7-i) * '* ')

for i in range(1, 9):
    print(f"{(2*i-1) * '*':^15}")
for i in range(7, 0, -1):
    print(f"{(2*i-1) * '*':^15}")

farenheit = -10
print('''Grader F     Grader C
======================''')
for i in range(13):
    celsius = (5 / 9) * farenheit - (160/9)
    print(f'{farenheit:5.0f}', end='  ')
    print(f'{celsius:14.1f}')
    farenheit += 10
print('''
      
      
      ''')

totalguess = []
'''
for i in range(3):
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
    print(f'Du klarade spelet på gissning nr. {i}.')
    totalguess.append(i)
print(totalguess)
print(f'Medelvärde antal gissningar: {sum(totalguess)/len(totalguess):.1f}')
'''

for i in range(100):
    num = random.randint(1,6)
    totalguess.append(num)

results =[0, 0, 0, 0, 0, 0]
for item in totalguess:
        results[item - 1] += 1


print('''  Värde       Antal infall
==========================''')
for i in range(len(results)):
    print(f'{i + 1:5.0f}', end='  ')
    print(f'{results[i - 1]:14.0f}')

print(f'Medelvärde: {sum(totalguess)/len(totalguess):.1f}')


'''
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

'''