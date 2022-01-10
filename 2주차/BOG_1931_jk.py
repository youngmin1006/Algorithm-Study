"""
1. 조건
회의실을 사용할 수 있는 회의의 최대 개수
회의의 시작시간과 끝나는 시간이 같을 수도 있다
2. 아이디어
회의의 최대개수를 구하기 위해선 가장 빨리 끝나면서 끝난 시점부터 가장 빨리 시작하는 것을 구해야 한다.
-> 끝나는 시간을 기준으로 오름차순 정렬 후 시작 시간을 오름차순 정렬
"""

from sys import stdin
input = stdin.readline

meeting = [ list(map(int, input().split())) for _ in range(int(input())) ]

meeting.sort(key = lambda x : (x[1], x[0])) # 끝나는 시간을 기준으로 오름차순 정렬후 시작시간을 기준으로 오름차순

meeting_cnt = 0 # 회의의 진행 횟수
last_meeting = 0 # 최근 미팅이 끝난 시간

for start, end in meeting:
    if last_meeting <= start: # 현재 시작시간이 최근 미팅이 끝난시간과 같거나 늦을 때
        last_meeting = end
        meeting_cnt += 1

print(meeting_cnt)
