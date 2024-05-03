d, n = int(input().split())
# 오븐의 깊이 d, 피자 반죽 수 n
oven = list(map(int, input().split()))
# 최상단부터 오븐의 지름
pizza = list(map(int, input().split()))
# 피자 반죽 순서대로
PinO = []

for o in range(d):
    if pizza[0] > o:
        PinO.append(pizza.pop())
        lastpizza = o
        d = o-1
        break

if pizza:
    print(0)
else:
    print(lastpizza)