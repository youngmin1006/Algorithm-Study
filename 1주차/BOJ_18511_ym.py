from itertools import product

N,Knum =  input().split()
Nsize = len(N)#N 의 자릿수 확인
N = int(N)
K = list(map(str, input().split()))#조합을 위해 string으로 받는다.

# print("K: ",K)
result = 0

while True:
    temp = list(product(K, repeat=Nsize))

    for i in temp:
        tempnum = int("".join(i)) #조합한 것을 숫자로
        if tempnum <= N:
            result = max(result,tempnum)
    if result == 0:
        Nsize-=1
    else:
        print(result)
        break




"""
#첫 시도. 자릿수 마다 비교해서, 가장 큰 자릿수 부터 채워나가는 방식으로 구현 -> 틀림 -> itertools의 product로 가능한 모든 경우의 수를 따져 조건에 맞는 수 찾는 방식으로 구현
N,Knum =  input().split()
Nsize = len(N)#N 의 자릿수 확인
N = int(N)
Knum = int(Knum)
K = list(map(int, input().split()))
K.sort(reverse = True)

# print("K: ",K)
result = [0 for i in range(Nsize)]

for i in range(Nsize):#i 번째 -> 10*(Nsize-i+1)의 자리 수
    x = Nsize-i #x번째 자리수
    # print("result : ",result)
    inum = (N//(10**(x-1)))%10
    for j in K:
        if inum == j:
            #첫자리 로 확정 다음 자리 확인
            # print("inum / j/ result :", inum, j, result)
            result[i] = j
            break

        elif inum >j:
            # print("inum / j/ result :",inum,j, result)
            #남은 자리 모두 가장 큰 수로 넣기
            result[i] = j
            result[i+1:] = [K[0] for k in range(Nsize-i-1)]
            break
        elif i!=0 and result[i] == 0: #655 3 /6 7 7 과 같은 경우를 위한것
            result[i-1] =0
            result[i:] = [K[0] for k in range(Nsize-i)]

    if result[-1] != 0:
        break
# print("result final: ",result)
sum = 0
for i in range(Nsize):
    sum += result[i]*(10**(Nsize-1-i))
print(sum)
"""