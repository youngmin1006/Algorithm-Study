num = int(input())

list = [[0 for i in range (2)]for j in range(num)]

for i in range(num):
    weight, height = input().split()
    list[i][0] = int(weight)
    list[i][1] = int(height)


rank = [0 for i in range(num)]
for i in range(num):
    rank_val = 1
    for j in range(num):
        if list[i][0] < list[j][0] and list[i][1] < list[j][1]:
            rank_val +=1
        else:
            continue
    rank[i] = rank_val
for i in range (num):
    print(rank[i],end=" ")


