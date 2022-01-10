from math import ceil, log
import sys
input = sys.stdin.readline


class Segment_tree:
    def __init__(self, arr):
        self.arr = arr
        self.depth = ceil(log(len(self.arr), 2) + 1)
        self.tree = [None] * (2 ** self.depth)
        self.init_tree(1, 0, len(self.arr) - 1)

    def init_tree(self, node, st, ed):
        if st == ed:
            self.tree[node] = self.arr[st], st
        else:
            mid = (st + ed) // 2
            left = self.init_tree(node * 2, st, mid)
            right = self.init_tree(node * 2 + 1, mid + 1, ed)
            self.tree[node] = max(left, right)
        return self.tree[node]

    def get_max_index(self):
        index = self.tree[1][1]
        self.arr[index] = 0
        self.init_tree(1, 0, len(self.arr) - 1)
        return index


n = int(input())
arr = list(map(int, input().split()))

ans, aim_index = 0, len(arr) - 1
segment_tree = Segment_tree(arr)

for i in range(len(arr)):
    ans += aim_index - segment_tree.get_max_index()
print(ans)