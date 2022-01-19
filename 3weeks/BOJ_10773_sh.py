# 제로
import sys
input = sys.stdin.readline

k = int(input())
l = [int(input()) for _ in range(k)]

stack = []

for i in l:
    if i != 0:
        stack.append(i)
    else:
        stack.pop()

print(sum(stack))