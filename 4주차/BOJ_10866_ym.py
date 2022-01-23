import sys
input = sys.stdin.readline

N = int(input())
com = [list(map(str,input().split())) for _ in range(N)]

stack = []

for i in range(N):
    if com[i][0] == 'push_front':
        stack.insert(0,int(com[i][1]))

    elif com[i][0] == 'push_back':
        stack.append(int(com[i][1]))

    elif com[i][0] == 'pop_front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(0))
    elif com[i][0] == 'pop_back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif com[i][0] == 'size':
        print(len(stack))
    elif com[i][0] == 'empty':
        if len(stack) == 0:
            print(1)
        else: print(0)
    elif com[i][0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif com[i][0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])