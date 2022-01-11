from collections import deque

import sys
input = sys.stdin.readline


def merge_sort(arr):
    cnt = 0

    def merge(st, ed):
        if st == ed:
            return deque([arr[st]])
        merge_arr = deque()
        mid = (st + ed) // 2
        left_arr = merge(st, mid)
        right_arr = merge(mid + 1, ed)

        nonlocal cnt
        while left_arr and right_arr:
            if left_arr[0] < right_arr[0]:
                merge_arr.append(left_arr.popleft())
            else:
                cnt += mid
                mid -= 1
                merge_arr.append(right_arr.popleft())
        if left_arr:
            merge_arr += left_arr
        else:
            merge_arr += right_arr
        return merge_arr
    return merge(0, len(arr) - 1)


arr = [int(input()) for _ in range(int(input()))]

for i in merge_sort(arr):
    print(i)
