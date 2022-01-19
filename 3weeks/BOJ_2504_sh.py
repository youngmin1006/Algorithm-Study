# 괄호의 값
# 문제 : 괄호열에 맞는 결과값을 출력

# 입력받기
import sys
input = sys.stdin.readline
str = list(input())
stack = []

# 괄호열 하나씩 돌아 가면서 검사
for s in str:
    # ( 나 [ 인 경우
    temp = 0
    if s == '(' or s == '[':
        stack.append(s)
    elif s == ')':
        if not stack:
            print(0)
            exit(0)
        else:
            while stack:
                p = stack.pop()
                if p == '[':
                    print(0)
                    exit(0)
                elif p == '(':
                    if temp == 0:
                        stack.append(2)
                    else:
                        stack.append(2 * temp)
                    break
                else:
                    temp += p
    elif s == ']':
        if not stack:
            print(0)
            exit(0)
        else:
            while stack:
                p = stack.pop()
                if p == '(':
                    print(0)
                    exit(0)
                elif p == '[':
                    if temp == 0:
                        stack.append(3)
                    else:
                        stack.append(3*temp)
                    break
                else:
                    temp += p

print(temp)
