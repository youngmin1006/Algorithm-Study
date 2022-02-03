import sys
input = sys.stdin.readline

str1 = list(input().strip())
str2 =list(input().strip())
length1 = len(str1)
length2 = len(str2)
arr = [[0]*(length2+1) for _ in range(length1+1)]

for i in range(length1):
    for j in range(length2):
        if str1[i] == str2[j]: #문자가 같으면 전에것에 1 더해줌
            arr[i+1][j+1] = arr[i][j]+1
        else:#다르면
            arr[i+1][j+1] = max(arr[i+1][j],arr[i][j+1])

print(arr[-1][-1])