from sys import stdin

input = stdin.readline

n = 9
tall = [ int(input()) for _ in range(n) ]

left_tall = sum(tall) - 100 # 100보다 오버된 키
flag = False # 이중반복문 탈출을 위한 flag

for i in range(n-1): # 0 ~ 7
    for j in range(i+1, n): # 1 ~ 8
        tmp1 = tall[i]
        tmp2 = tall[j]

        if (tmp1 + tmp2) == left_tall:
            flag = True
            break

    if flag:
        break

tall.remove(tmp1)
tall.remove(tmp2)

for i in sorted(tall):
    print(i)
