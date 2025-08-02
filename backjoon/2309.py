from itertools import combinations

height = [int(input()) for _ in range(9)]
for comb in combinations(height, 7):
    if sum(comb) == 100:
        for i in sorted(comb):
            print(i)
        break