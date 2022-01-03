

N,Z,M =  input().split()
N = int(N)#필드 수
Z = int(Z)#도착해야하는 필드 번호
M = int(M)#장애물 있는 필드 수
trap = set(map(int, input().split()))

if Z==N:
    Z=0

'''
#시간초과 
def solve(k):
    current = 1
    while True:
        current += k
        if current >= N:
            current = current%N
        if current in trap:
            return 0
        elif current == Z:
            return 1
'''
def solve(k):
    path = [(1+k*x)%N for x in range(N)]
    for current in path:
        if current in trap:
            return 0
        elif current == Z:
            return 1

for i in range(1,N):# Z까지만 검사하면 된다고 생각 했지만, 장애물로인해 k 가 Z 보다 더 클 수 도 있다는것을 생각하지 못함.
    if solve(i)==1:
        print(i)
        break