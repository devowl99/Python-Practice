import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    word = input().strip()
    
wlen = len(word)
gw = 0

for i in range(wlen-2):
     for j in range(i+2, wlen):
        if word(i) != word(j):
            gw += 1