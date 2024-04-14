# 왜 안될까

import sys
input = sys.stdin.readline

n = int(input())
word = []
gw = 0

for _ in range(n):
    word.append(input().strip())

for i in word:
    ilen = len(i)
    is_gw = True

    if ilen <= 2 or len(set(i)) == 1:
        gw += 1
        # print('case1 : ' + i)
    else:
        for j in range(ilen-2):
            for k in range(j+2, ilen):
                if i[j] == i[k]:
                    is_gw = False
                    break
            
        if is_gw:
            gw += 1
            # print('case2 : ' + i)
        ngw = 0

print(gw)