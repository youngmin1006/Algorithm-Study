input_str = input()

cnt = 0
depth = 0
for i in range(len(input_str)):
    if input_str[i] =='(':
        depth +=1
        cnt += 1

    else:#')'
        if input_str[i-1] == "(":#레이져인 경우
            depth -= 1
            cnt -= 1
            cnt += depth
        else: # 막대기가 끝나는 경우
            depth -=1

print(cnt)