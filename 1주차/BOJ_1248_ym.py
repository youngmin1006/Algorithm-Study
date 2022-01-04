N =  int(input())
con = list(input())#N*(N+1)/2 개
S= [[0]*N for i in range(N)]
result = [0 for i in range(N)]
for i in range(N):
    for j in range(i,N):
        str = con.pop(0)
        if str == "+":
            S[i][j] = 1
        elif str == "-":
            S[i][j] = -1
        elif str == "0":
            S[i][j] = 0

def check(idx): #0~idx 까지의 수의 합의 부호가 S와 맞는지 확인
    sum = 0 #result[idx] ~ result[0] 까지의 합 =>sum 과 S[i][idx] 를 비교
    for i in range(idx,-1,-1):
        sum+=result[i]
        if sum == 0 and S[i][idx] !=0:
            return 0
        elif sum > 0 and S[i][idx] != 1:
            return 0
        elif sum < 0 and S[i][idx] != -1:
            return 0
    return 1

def solve(idx):#idx 번째 수를 찾음 (0~N-1)
    if idx == N:
        return 1
    if S[idx][idx] == 1:
        for i in range(1, 11):
            result[idx] = i
            if check(idx) ==1  and solve(idx+1):# 체크와 다음 인덱스 확인,(결국 끝 까지 의 인덱스 확인) 이 모두 조건을 만족할 때 끝난다.
                return 1
    elif S[idx][idx] == -1:
        for i in range(1, 11):
            result[idx] = -i
            if check(idx) ==1 and solve(idx+1):
                return 1
    elif S[idx][idx] == 0:
        result[idx] = 0
        return  solve(idx+1)
    return 0

solve(0)
for i in range(N):
    print(result[i],end=" ")
