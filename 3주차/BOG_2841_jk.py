from sys import stdin
input = stdin.readline

n, p = map(int, input().split())
melody = [ list(map(int, input().split())) for _ in range(n) ]
stack = [ [] for _ in range(n+1) ]
finger_cnt = 0

for num, fret in melody:

    if not stack[num]: # 줄을 누르고 있지 않은 상태라면
        stack[num].append(fret) # 프렛의 번호를 넣어주고
        finger_cnt += 1 # 프렛을 누르고 횟수를 더해줌.

    else: # 이미 줄을 누르고 있는 상태라면면
        if fret < stack[num][-1]: # 프렛이 이미 누르고 있는 프렛보다 작은 경우
            while stack[num]: # 프렛이 이미 누르고 있는 프렛보다 클때까지 손을 뗀다
                if fret >= stack[num][-1]:
                    break
                stack[num].pop()
                finger_cnt += 1

            if len(stack[num]) and fret == stack[num][-1]: # 스택이 비어있다면 값을 비교할 게 없으니 확인해준다.
                continue
            else:
                stack[num].append(fret)
                finger_cnt += 1

        elif fret > stack[num][-1]: # 프렛이 이미 누르고 있는 프렛보다 큰 경우
            stack[num].append(fret)
            finger_cnt += 1

        else: # 프렛이 이미 누르고 있는 프렛과 같은 경우
            continue

print(finger_cnt)
