import sys
input = sys.stdin.readline
N,K = map(int,input().split())
num = [0]*1000001
max_num = 0
for i in range(N):
    g,x =  map(int,input().split())
    num[x] = g
    max_num = max(max_num,x)

res = []
step = 2*K+1
window = sum(num[:step])
res = window
for i in range(step,max_num+1):
    # res.append(sum(num[i-(2*K):i+1])) #런타임 에러, 윈도우 따로 만들어 처리 매번 리스트 슬라이싱X, 전 윈도우에서 앞에것 빼고, 새로운것 더하는 것이 효율적
    window +=num[i] -num[i-step]
    res = max(res,window)
print(res)

