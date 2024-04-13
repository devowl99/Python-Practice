import sys
input = sys.stdin.readline

txt = input()
stack = []

for i in txt:
    if i == '.':
        break
    elif i == '(' or i == '[':
        stack.append(i)

    if stack[-1] == '(' and i == ')':
        stack.pop()
        print('yes')
    elif stack[-1] == '[' and i == ']':
        stack.pop()
        print('yes')
    
    # 미완(과제)