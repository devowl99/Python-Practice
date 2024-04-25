word = input()
change = []

for i in word:
    if i >= 'a' and i <= 'z':
        change.append(i.upper())
    else:
        change.append(i.lower())

print(''.join(change))

# ord() : 문자 -> ASCII 변환
# chr() : ASCII -> 문자 변환