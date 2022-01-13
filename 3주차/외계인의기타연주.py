import sys
input = sys.stdin.readline
N, P = map(int, input().split(' '))
melody = [list(map(int, input().split(' '))) for i in range(N)]
melody.sort(key=lambda x : x[0]) # 앞만 우선 정렬
answer = 0
stack = [] # 현재 손가락이 잡고 있는 기타줄
for gs, p in melody :
    if stack :
        n = len(stack)
        for i in range(n) :
            stack_gs, stack_p = stack[-1]
            if gs == stack_gs :
                if p < stack_p :
                    stack.pop()
                    answer+=1
                elif p == stack_p :
                    break
                else :
                    stack.append([gs, p])
                    answer+=1
                    break
            else :
                stack.append([gs, p])
                answer+=1
                break
        else :
            if not stack:
                stack.append([gs, p])
                answer+=1
    else :
        stack.append([gs, p])
        answer+=1

print(answer)
