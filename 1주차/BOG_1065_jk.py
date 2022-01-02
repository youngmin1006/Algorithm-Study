# 1부터 99까지는 무조건 한수 이므로 값을 출력한다.
# 100 이상부터 조건식을 이용해 한수를 체크해 나간다.

from sys import stdin

n = int(input())

cnt = 0

if n < 100:
    cnt = n
else:
    cnt = 99
    for i in range(100, n+1):
        tmp = []
        for j in str(i):
            tmp.append(int(j))

        if (tmp[2] - tmp[1] == tmp[1] - tmp[0]):
            cnt += 1

print(cnt)
