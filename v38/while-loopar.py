print("Figur A\n")
max_rows = 6
max_cols = max_rows
current_row = 0
while current_row <= max_rows:
    current_col = 0
    while current_col <= max_cols:
        print("*", end="  ")
        current_col += 1
    print()
    current_row += 1
print()

max_rows = 6
max_cols = max_rows
current_row = 0
while current_row <= max_rows:
    current_col = 0
    while current_col <= max_cols:
        if current_col % 2 != 0 and current_row % 2 != 0:
            print(" ", end = "  ")
        else:
            print("*", end="  ")
        current_col += 1
    print()
    current_row += 1
print()

'''max_rows = 6
max_cols = max_rows
current_row = 0
while current_row <= max_rows:
    current_col = 0
    while current_col <= max_cols:
        if current_col % 2 == 0 and current_row  % 2 == 1:
            print('*', end='  ')
        elif current_col % 2 == 0 and current_row % 2 == 0:
            print('', end='  ')
        elif current_col % 2 == 1 and current_row % 2 == 1:
            print('', end='  ')
        elif current_col % 2 == 1 and current_row % 2 == 0:
            print('*', end='  ')
        current_col += 1
    print()
    current_row += 1
# print()'''

max_rows = 6
max_cols = max_rows
current_row = 0
while current_row <= max_rows:
    current_col = 0
    while current_col <= max_cols:
        if current_col % 2 == 0:
            if current_row % 2 == 1:
                print('*', end='  ')
            else:
                print(' ', end='  ')
        else:
            if current_row % 2 == 1:
                print(' ', end='  ')
            else:
                print('*', end='  ')
        current_col += 1
    print()
    current_row += 1
print()