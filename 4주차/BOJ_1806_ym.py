import sys
input = sys.stdin.readline
N,S = map(int,input().split())
arr = list(map(int,input().split()))

sum = 0
l,r = 0,0
ans = sys.maxsize
while True:
    if sum >= S:
        ans = min(ans,r-l)
        sum -= arr[l]
        l+=1
    elif r == N:
        break
    else:
        sum += arr[r]
        r+=1

if ans == sys.maxsize:
    print(0)
else: print(ans)
