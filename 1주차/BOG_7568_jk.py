from sys import stdin

input = stdin.readline

n = int(input())
size = []
res = []

for _ in range(n):
    a, b = map(int, input().split())
    size.append((a, b))

for i in range(n):
    rank = 1 # 모든 사람의 시작은 1등

    for j in range(n):
        if size[i][0] < size[j][0] and size[i][1] < size[j][1]: # 반복문을 돌면서 자기보다 큰 사람이 있으면 등수 낮추기
            rank += 1

    res.append(rank)

print(*res)
