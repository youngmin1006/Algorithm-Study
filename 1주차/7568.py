import sys
input = sys.stdin.readline

person_line = [list(map(int, input().split())) for _ in range(int(input()))]

for i in person_line:
    rank = 1
    for j in person_line:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')