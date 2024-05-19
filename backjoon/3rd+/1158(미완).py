n, k = map(int, input().split())

people = [1 for _ in range(n)]
for num in range(1, n):
    people[num] = num + 1

target = 0
plen = n
print('<', end='')
while True:
    target += k
    if target > plen:
        plen = len(people)
        target %= plen
    
    print(people.pop(target), end = '')
    
    if people:
        print(',', end=' ')
    else:
        break
print('>')