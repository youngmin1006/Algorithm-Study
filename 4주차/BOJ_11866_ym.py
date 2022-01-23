N,K = map(int,input().split())
num = [i for i in range(1,N+1)]
res = []
temp = K - 1
while num:
    idx = temp%len(num)
    res.append(num.pop(idx))
    temp = idx + K -1
str = ", ".join([str(i) for i in res])
print("<",str,">",sep="")