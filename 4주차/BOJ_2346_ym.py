from collections import deque
N = int(input())
num = deque(enumerate(map(int,input().split())))

while num:
    idx, x = num.popleft()
    print(idx+1,end=" ")
    if num and x > 0:
        for i in range(x-1):num.append(num.popleft()) # num.rotate(-(num-1))
    elif num and x < 0:
        for i in range(abs(x)):num.insert(0,num.pop())#num.rotate(abs(num))
