import sys
input = sys.stdin.readline

def bubble_sort(n, nl):
    for i in range(0, n-1):
        for j in range(i+1, n):
            if nl[i] > nl[j]:
                nl[i], nl[j] = nl[j], nl[i]

n = int(input())
nl = list()

for i in range(n):
    nl.append(int(input()))

bubble_sort(len(nl), nl)

for i in range(n):
    print(nl[i])