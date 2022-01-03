input_num = 9
input_list = [int(input()) for i in range(input_num)]

sum_value = sum(input_list)
temp_1, temp_2 = 0, 0

for i in range(input_num):
    for j in range(i+1, input_num):
        if (sum_value - (input_list[i] + input_list[j])) == 100:
            temp_1 = input_list[i]
            temp_2 = input_list[j]

input_list.remove(temp_1)
input_list.remove(temp_2)

print('\n'.join(map(str, sorted(input_list))))