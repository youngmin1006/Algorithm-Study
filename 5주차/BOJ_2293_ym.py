n,k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
arr = [0 for i in range(k+1)]
arr[0] = 1
for i in coin:
    for j in range(1,k+1):
        if j-i >= 0:
            arr[j] += arr[j-i]

print(arr[k])