# 가장 큰 수

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True) # 내림차순 정렬
    answer = str(int(''.join(numbers))) 
    return answer
