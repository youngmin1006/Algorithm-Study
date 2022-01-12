import sys
N = int(input())
score = [list(sys.stdin.readline().split()) for _ in range(N)] #string 으로 받음. 이름때문에
score.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])) #정수형으로 바꿔주고 정렬
for i in score:
    sys.stdout.write(i[0]+'\n')
#문자열 출력은 반복하지 말고 가능한 한번에 출력하기.