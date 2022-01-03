import sys
input = sys.stdin.readline


def number_judge(num):
    if num <= 99: return 1

    num_line = []
    while num:
        num_line.append(num % 10)
        num //= 10

    diff = num_line[1] - num_line[0]
    for i in range(2, len(num_line)):
        if diff != (num_line[i] - num_line[i - 1]):
            return 0
    return 1


ans = 0
for i in range(1, int(input()) + 1):
    ans += number_judge(i)
print(ans)