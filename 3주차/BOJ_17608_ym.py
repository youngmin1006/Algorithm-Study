import sys
input = sys.stdin.readline

N = int(input())
stack = [int(input()) for _ in range(N)]

max = stack[-1]
cnt = 1
for i in range(N-1,-1,-1):
    if stack[i]>max:
        cnt+=1
        max = stack[i]
print(cnt)