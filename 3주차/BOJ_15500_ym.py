N =  int(input())
stacka = list(map(int,input().split()))
stackb = []
result = []
cnt = 0
max = N

def hanoi(check,max):
    global cnt
    if not stacka and not stackb:
        return
    if check == 1:
        temp = max
        while(stacka):
            num_a = stacka.pop()
            if num_a == max:
                result.append([1,3])
                cnt+=1
                max -=1
            else:
                stackb.append(num_a)
                result.append([1,2])
                cnt+=1
        if max == temp:
            max -=1
        hanoi(2,max)

    else:
        temp = max
        while (stackb):
            num_b = stackb.pop()
            if num_b == max:
                result.append([2,3])
                cnt += 1
                max -= 1
            else:
                stacka.append(num_b)
                result.append([2,1])
                cnt += 1
        if max == temp:
            max -= 1
        hanoi(1,max)

hanoi(1,N)
print(cnt)
for a,b in result:
    print(a,b)

