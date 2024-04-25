import sys
input = sys.stdin.readline

def quick_sort(nl):
    if len(nl) <= 1:
        return nl

    piv = nl[0]
    big = []
    small = []

    for i in nl[1:]:
        if i < piv:
            small.append(i)
        else:
            big.append(i)

    return quick_sort(small) + [piv] + quick_sort(big)

n = int(input())
nl = []

for i in range(n):
    nl.append(int(input()))

for i in quick_sort(nl):
    print(i)

# 메모리 초과