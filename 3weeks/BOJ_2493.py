# 탑
# 수신 받는 탑의 인덱스 출력

import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))
stack = []
idx = [0 for i in range(n)]

for i in range(len(top)):
    while stack:
        if stack[-1][1] > top[i]:
            idx[i] = stack[-1][0] + 1
            break
        else: # 오른쪽 탑의 높이가 더 높은 경우
            stack.pop()
    stack.append([i, top[i]]) # 일단 처음엔 [인덱스, 높이] append

print(*idx)

