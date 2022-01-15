# 막대기

import sys
input = sys.stdin.readline

n = int(input())
height = [int(input()) for _ in range(n)]

t = height.pop()
count = 1
for _ in range(n-1):
    nt = height.pop()
    if t < nt:
        count += 1
        t = nt

print(count)