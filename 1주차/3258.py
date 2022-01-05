import sys
input = sys.stdin.readline


def simulate(jump):
    st, end = 0, end_point - 1
    visit = [0] * field_num

    while st != end:
        st = (st + jump) % field_num
        if (st + 1) in obstacle or visit[st]:
            break
        visit[st] = True
    else: return True
    return False


field_num, end_point, obstacle_num = map(int, input().split())
obstacle = list(map(int, input().split()))

for jump in range(1, end_point):
    if simulate(jump):
        print(jump)
        break