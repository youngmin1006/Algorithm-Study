n = int(input())
nqueen = [0 for i in range(n)]
result = 0
def check(k):
    for i in range(k):#n이 아니라 k여야 한다. k 행만 확인 해야 하기 때문(전채 열을 확인 X)
        if nqueen[k] == nqueen[i] or k-i == abs(nqueen[k] - nqueen[i]):
            return 0
    return 1

def queen(k):#k행에 말 놓기
    global result
    if k == n: #마지막 행까지 놓고 난 후 , 종료조건
        result += 1 #경우의 수 1 증가 -> 전역변수
        return 0
    for i in range(n):
        nqueen[k] = i
        if check(k) == 1:
            queen(k+1)
        else:
            continue

queen(0)
print(result)