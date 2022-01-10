# 치킨 TOP N

n = int(input())
input_list = list(map(int, input().split()))
k = int(input())

temp_list = []
size = n//k # k명 당 정렬해야 하는 배열의 크기
for i in range(0, n, size):
    temp_list += sorted(input_list[i:i+size])
print(" ".join(str(i) for i in temp_list))