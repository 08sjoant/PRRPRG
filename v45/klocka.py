import time as rolex
clock = [0, 0, 0, 0, 0, 0, 0]
base = [2, 10, 6, 10, 6, 10]

while len(clock) > 0:
    output = ''
    if clock[0] > 0:
        output = f'{clock[0]}:'
    for i in range(1, len(clock)):
        output = output + str(clock[i])
        if i % 2 == 0 and i < 6:
            output = output + ':'
    print(output)
    rolex.sleep(0)
    clock[-1] += 1
    for i in range(1, len(base)):
        if clock[0-i] >= base[0-i]:
            clock[0-i] = 0
            clock[-1-i] += 1
    if clock[1] == 2 and clock[2] == 4:
        clock[0] += 1
        for i in range(1, 3):
            clock[i] = 0
