import time as rolex
clock = [0, 0, 0, 0, 0, 0, 0]
output = ''

while len(clock) > 0:
    if clock[0] < 1:
        for i in range(1, len(clock)):
            output = output + str(clock[i])
    else:
        for i in range(len(clock)):
            output = output + str(clock[i])
    print(output)
    break