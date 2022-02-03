import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().split()))
m = int(input())

arr = [[0]*n for _ in range(n)]

for i in range(n):#0~ n-1 까지, => 시작 전까지 => n-i = 시작 수
    for s in range(n-i):#start
        e = s+i #end

        #펠린드롬 검사
        if s == e:#시작과 끝이 같으면 글자수 한개 => 무저건 펠린드롬
            arr[s][e] = 1
        elif num[s] == num[e]:#시작수 == 끝 수
            if s+1 == e:#두글자 짜리면 펠
                arr[s][e] = 1
            elif arr[s+1][e-1]==1:
                arr[s][e] = 1
ans = []
for i in range(m):
    start,end = map(int,input().split())
    ans.append(arr[start-1][end-1])

print(*ans,sep="\n")