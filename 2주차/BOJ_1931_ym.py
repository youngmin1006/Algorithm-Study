import sys
N = int(input())
conference = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

res = 0 #몇개의 회의를 잡았는지에 대한 결과
#끝시간 오름차순 , 시작시간 오름차순으로 정렬
now = 0 #현재 시간
conference.sort(key=lambda x: (x[1],x[0]))
#print(conference)
for time in conference:
    if time[0] < now:
        continue
    else:
        res +=1
        now = time[1]

print(res)