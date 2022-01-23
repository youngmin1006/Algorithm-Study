import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    command = input()
    command.replace('RR', '')
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    if n == 0: arr = []
    check ,cnt,left,right = 0,0,0,0

    for s in command:
        if s == "R": cnt+=1
        elif s == "D":
            if cnt % 2 == 0: left += 1
            else: right += 1
    if left+right>n : print("error")

    else:
        arr = arr[left:n-right]
        if cnt % 2 == 0: sys.stdout.write('[' + ','.join(arr) + ']\n')
        else:
            str = '[' + ','.join(arr[::-1]) + ']\n'
            sys.stdout.write(str)

