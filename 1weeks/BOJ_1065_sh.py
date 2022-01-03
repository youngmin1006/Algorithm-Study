def hansu(input_num):
    count, sub_1, sub_2 = 0, 0, 0
    for i in range(1, input_num + 1):
        if i < 100:
            count += 1
        else:
            input_list = list(map(int, str(i)))
            sub_1 = input_list[0] - input_list[1]
            sub_2 = input_list[1] - input_list[2]
            if sub_1 == sub_2:
                count += 1
    return count

input_num = int(input())

if input_num < 0 or input_num > 1000:
    print("입력 범위를 벗어났습니다.")
    exit()

print(hansu(input_num))



