# FrogJmp
# x에서 y까지 이동할때, 점프 횟수 구하기

def solution(X, Y, D):
    distance = Y - X
    jump = (Y - X) // D
    rest = (Y - X) % D

    if (rest != 0):
        jump += 1

    return jump

# PermMissingElem
# 빠진 정수 찾기

def solution(A):
    A.sort()
    length = len(A)

    if length == 0:
        return 1

    for i in range(0, length): # index검사는 length-1까지
        if A[i] != i + 1:
            return i + 1

    return A[length - 1] + 1 # 마지막인 경우

# TapeEquilibrium
# 함수를 두개로 나누었을 때 각각의 합의 차의 최소가 되는 p값

import sys

def solution(A):
    sum_1, sum_2 = 0, sum(A) # 초기 상태
    min_dist = sys.maxsize # 최대 정수값
    if len(A) == 1:
        return A[0]

    for i in A[:-1]: # 마지막 제외 검사
        sum_1 += i
        sum_2 -= i
        min_dist = min(min_dist, abs(sum_1 - sum_2)) # 결국 차의 절대값의 최소값이 남을 것

    return  min_dist