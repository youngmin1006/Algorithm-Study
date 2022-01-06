import sys
N = int(input())
num = [int(sys.stdin.readline()) for _ in range(N) ]
num.sort() #sort 함수 : O(nlog(n))

for i in num:
    sys.stdout.write(str(i)+'\n')