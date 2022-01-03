input_num = int(input())
people_info_list = []

for _ in range(input_num):
    weight, height = map(int, input().split()) #한꺼번에 int형으로 바꾸기
    people_info_list.append((weight, height))

for i in people_info_list:
    rank = 1
    for j in people_info_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")