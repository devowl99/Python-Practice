# 왜 안될까
n = int(input())
word = []
gw = 0

for _ in range(n):
    word.append(input())

for i in word:
    ilen = len(i)
    is_gw = True

    if ilen > 2 and len(set(i)) != 1:
        for j in range(ilen-2):
            for k in range(j+2, ilen):
                if i[j] == i[k]:
                    is_gw = False
                    break    
            if not is_gw:
                break
    if is_gw:
        gw += 1

print(gw)