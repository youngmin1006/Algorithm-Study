import sys
input = sys.stdin.readline


stu_grade = [input().split() for _ in range(int(input()))]

for name in sorted(stu_grade, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])):
    print(name[0])