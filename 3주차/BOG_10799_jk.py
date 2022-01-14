"""
아이디어 : 문제 이해가 어려웠다. 이해만 된다면 쉽게 풀 수 있었던 문제인 것 같다.
스택에 차곡차곡 쌓은 다음 ')' 즉, 뺄때 이전 값이 무엇이냐에 따라 더해주는 값을 달리 해야 한다.

시간소요 : 43분
"""

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
