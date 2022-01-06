import sys

n = int(input())

list = [int(sys.stdin.readline()) for _ in range(n)]

for i in sorted(list):
    print(i)