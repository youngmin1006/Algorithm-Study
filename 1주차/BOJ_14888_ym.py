
N = int(input())#수의 갯수
A = list(map(int,input().split()))#수 N 개
Op = list(map(int,input().split()))#+,-,*,// 의 갯수

result = []#답을 모두 저장

def solve(idx,current, plus,minus,multi,div):#계산할 수의 인덱스(1) , 쓸 연산자 인덱스(0), 각 연산자 남은 수
    global min_num,max_num
    if idx == N:
        result.append(current)
        return 1
    else:
        if plus > 0:  # +연산이 남아있을 때
            solve(idx+1,current+A[idx],plus-1,minus,multi,div)
        if minus > 0:
            solve(idx + 1, current - A[idx], plus, minus-1, multi, div)
        if multi > 0:
            solve(idx + 1, current * A[idx], plus, minus, multi-1, div)
        if div > 0:
            solve(idx + 1, int(current / A[idx]), plus, minus, multi, div-1)
    return 0

solve(1,A[0],Op[0],Op[1],Op[2],Op[3])
print(max(result))
print(min(result))

