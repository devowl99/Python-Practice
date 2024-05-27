import sys
input = sys.stdin.readline

n, m = map(int, input().split())

word = []
check = []
count = 0
for _ in range(n):
    word.append(input().strip())
for _ in range(m):
    check.append(input().strip())

for i in word:
    for j in check:
        if i == j:
            count += 1
            break

print(count)