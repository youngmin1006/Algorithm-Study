import sys
input = sys.stdin.readline


def dwarf_combi(num):
    for i in range(1 << num + 1):
        ans = []
        height_sum = 0
        for j in range(9):
            if i & (1 << j):
                height_sum += dwarf_line[j]
                ans.append(j)
        if height_sum == 100 and len(ans) == 7: return ans


dwarf_line = sorted([int(input()) for _ in range(9)])

for i in dwarf_combi(9):
    print(dwarf_line[i])

