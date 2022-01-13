inputstr = list(input())
stack = []
answer = 0
res = 1
for i in range(len(inputstr)):
    if inputstr[i] == '(':
        stack.append(inputstr[i])
        res*=2
    elif inputstr[i] == '[':
        stack.append(inputstr[i])
        res*=3
    elif inputstr[i] == ']':
        if  not stack or stack[-1] == '(':#스택이 비어있거나 전이  꼴이 다른 열린 괄호 일 때
            answer = 0
            break
        if inputstr[i-1] == '[':
            answer += res
        stack.pop()
        res //=3
    else: #')'
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if inputstr[i-1] == '(':
            answer += res
        stack.pop()
        res //= 2
if stack:
    answer = 0
print(answer)