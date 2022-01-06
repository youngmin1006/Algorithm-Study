from sys import stdin
input = stdin.readline

array = [ int(input()) for _ in range(int(input()))]

for i in sorted(array):
    print(i)
