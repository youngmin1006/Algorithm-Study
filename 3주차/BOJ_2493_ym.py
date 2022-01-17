import sys
N = int(input())
num = list(map(int,sys.stdin.readline().split()))
stack = []
res = []
for i in range(N):
    if i == 0:
        stack.append([i,num[i]])
        res.append(0)
        continue;
    while stack and stack[-1][1] < num[i]:#수신 가능한게 나올때 까지 pop
        stack.pop()
    if not stack:
        res.append(0)
    else: res.append(stack[-1][0]+1)
    stack.append([i,num[i]])

print(*res)






# def laser(n):#스택과 비교할 인덱스
#     for i in range(n-1,-1,-1):
#         if stack[i] >= stack[n]:
#             return i+1
#     return 0
# for i in range(N):
#     print(laser(i),end = " ")
