import sys
input = sys.stdin.readline

N, P = map(int,input().split())
melody = [list(map(int,input().split())) for _ in range(N)]
stack = [[] for i in range(7)]
cnt = 0

for s,p in melody:
    if not stack[s]:
        stack[s].append(p)
        cnt +=1
    else:
        while stack[s] and stack[s][-1] > p:
            stack[s].pop()
            cnt+=1
        if stack[s] and stack[s][-1] == p:
            continue
        else:
            stack[s].append(p)
            cnt+=1

print(cnt)

