import sys
input = sys.stdin.readline
N,K = map(int,input().split())
num = list(map(int,input().split()))
ryan = []
res = []
for i in range(N):
    if num[i] == 1:
        ryan.append(i)

start = 0
end = K-1
ans = sys.maxsize
while end < len(ryan):
    temp = ryan[end]-ryan[start]+1
    ans = min(ans,temp)
    start+=1
    end +=1
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
