import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
person = int(input())

per_sort = n // person

for i in range(0, n, per_sort):
    arr[i:i + per_sort] = sorted(arr[i:i + per_sort])
print(*arr)

