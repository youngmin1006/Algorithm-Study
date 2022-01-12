# 처음 풀이 (시간초과)

from itertools import permutations

def solution(numbers):
    
    numbers = list(map(str, numbers))
    numbers = list(map(''.join, permutations(numbers))) # permutations(배열, 인자값) : 인자값 생략시 전체 경우에 대하여 탐색
    
    return str(max(list(map(int, numbers))))
    
# 정답 풀이

def solution(numbers):
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x*3, reverse=True)
    
    # int 해주는 이유 : '0000'일때 '0'이 나오도록 해야함.
    return str(int(''.join(numbers)))
