def f(n):
    varde = 1
    for i in (1, n+1):
        varde = varde * i
    return varde

x = f(5)
print(x)