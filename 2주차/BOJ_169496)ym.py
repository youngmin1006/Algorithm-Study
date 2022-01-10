N =  int(input())
num = [list(map(str,input().split()))]
num.append([0 for _ in range(N)])

num = [list(x) for x in zip(*num)] #행렬 전치 연산자

for n in num:
    temp_arr = [0 for _ in range(10)]

    str_idx = 0
    for i in range(10): #비교할 수 만들기 ( 수 반복해서 채워주기 )( 10**(10-1) 만큼) #처음에는 가장 길이가 긴 자릿수에 맞췄는데, 예외 생김
        temp_arr[i] = n[0][str_idx]
        str_idx+=1
        if str_idx >= len(n[0]):
            str_idx = 0

    n[1] = int("".join(temp_arr))
    #n[0] = int(n[0])#정수형으로 만들어 주기

num.sort(key = lambda x: (-x[1]))
result = [x[0] for x in num]
# print(result)

# 정렬된 배열로 수 구하기
res = "".join(result)
print(int(res))

