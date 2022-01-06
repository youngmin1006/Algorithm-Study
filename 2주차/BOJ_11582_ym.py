N = int(input())
chicken = list(map(int, input().split()))
check = int(input())

#각각의 원소를 리스트로 변환 1차원 ->2차원
res = []
for i in chicken:
    res.append([i])

def solve(n):
    global res
    if n == 0: #끝 까지 다 돌았을 때 종료조건
        return
    if n*2 == check:#k 단계를 완료한 상태 출력 후 종료 결과를 완료한 상태를 출력해야 하므로 n*2 가 check 와 같은지 검사.
        for i in res:
            for j in i:
                print(j, end=" ")
        return
    tempres = []#임시 결과 리스트
    for i in range(n):#두 개 선택후 정렬
        temp = res[2 * i] + res[2 * i + 1]
        temp.sort()
        tempres.append(temp)
    res = tempres
    solve(n // 2)

solve(N//2)