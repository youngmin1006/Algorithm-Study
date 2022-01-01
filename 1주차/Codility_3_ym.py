#3-1번
#https://app.codility.com/demo/results/trainingDUW8SC-9P6/

def solution(X, Y, D):
    # write your code in Python 3.6
    res = (Y-X)//D
    if (Y-X)%D != 0:
        res +=1
    return res

#3-2번
#https://app.codility.com/demo/results/trainingDEDK49-RFC/
def solution(A):
    # write your code in Python 3.6
    length = len(A)#len이 4면 1~5 까지 수 가능
    isused = [0 for i in range(length+2)]

    for i in range(length):
        isused[A[i]] = 1

    for i in range(1,length+2):
        if isused[i] == 0:
            return i

#3-3번
#https://app.codility.com/demo/results/trainingQ5JZ5V-QHJ/

def solution(A):
    # write your code in Python 3.6
    sumA = 0
    sumB = sum(A)
    res = 100000
    for i in range(len(A)-1):
        sumA += A[i]
        sumB -= A[i]
        diff = abs(sumA-sumB)
        res = min(res,diff)
    return res