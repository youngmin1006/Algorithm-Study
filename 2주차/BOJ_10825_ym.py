import sys
N = int(input())
score = [list(sys.stdin.readline().split()) for _ in range(N)]
score.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in score:
    sys.stdout.write(i[0]+'\n')
