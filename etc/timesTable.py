n = 1
while n <= 9:
    for i in range(1, 10):
        for j in range(3):
            print("%2d * %d = %2d   " % (n + j,  i, (n + j) * i), end="")
        print()
    print()
    n += 3