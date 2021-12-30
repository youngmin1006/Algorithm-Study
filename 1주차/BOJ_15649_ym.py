N ,M = input().split()
N = int(N)
M = int(M)

list = [0 for i in range(M)]
isused =  [0 for i in range(N)] # 1~ N 까지의 숫자가 쓰였느냐 -> n 번째 자리수를 정한다.

def select(k):# k번째 자리를 정함
    if k == M:#재귀 종료조건, 리스트 출력
        for i in range(M):  # 리스트 출력
            print(list[i], end=" ")
        print()
        return 0
    for i in range(N):#(0~N-1)
        if( isused[i] == 0):
            isused[i] =1
            list[k] = i+1
            select(k+1)
            isused[i] =0

select(0)

