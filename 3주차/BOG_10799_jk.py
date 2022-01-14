from sys import stdin
input = stdin.readline

parenthesis = list(input())
stack = []
ans = 0

for x in parenthesis:

    if x == '(':
        stack.append(x)

    elif x == ')':
        stack.pop()

        if peek == '(':
            ans += len(stack)
        else:
            ans += 1

    peek = x # 이전 값을 기록해놓아야 한다. 이전값이 '(', ')' 무엇인지에 따라 값이 다름



print(ans)
