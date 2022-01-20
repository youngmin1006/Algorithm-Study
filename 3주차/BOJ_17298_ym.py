N = int(input())
num = list(map(int,input().split()))
res = [-1]*N
stack = []#인덱스 저장
for i in range(N):
    while stack and (num[stack[-1]] < num[i]):
        res[stack.pop()] = num[i]
    stack.append(i)

print(*res)
