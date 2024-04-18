n = 1
selfnum = [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97]
notsn = []

for _ in range(10000):
    if n >= 10 and n < 100:
        cons = n + n/10 + n%10
        notsn.append(cons)
    if n >= 100 and n < 1000:
        cons = n + n/100 + n/10 + n%10
        notsn.append(cons)
    elif n >= 1000 and n < 10000:
        cons = n + n/100 + n/10 + n%10
        notsn.append(cons)
    n += 1

for i in range(1,10001):
    if i not in notsn:
        selfnum.append(i)

for i in selfnum:
    print(i)