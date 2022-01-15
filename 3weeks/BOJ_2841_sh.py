# 외계인의 기타 연주

import sys
input = sys.stdin.readline

n, p = map(int, input().split())
sound = [list(map(int, input().split())) for _ in range(n)]

stack = [[] for _ in range(7)] 
count = 0

for line, fret in sound: 
   
    # 비어있는 경우
    if len(stack[line]) == 0:
        stack[line].append(fret)
        count += 1

    # 비어있지 않은 경우
    else:
        if fret > stack[line][-1]:
            stack[line].append(fret)
            count += 1
        elif fret == stack[line][-1]:
            continue
        else:
            while len(stack[line]) != 0 and fret < stack[line][-1]:
                stack[line].pop()
                count += 1
            if len(stack[line]) != 0 and fret == stack[line][-1]: # 지금 연주되고 있다는 의미
                continue
            stack[line].append(fret)
            count += 1

print(count)
