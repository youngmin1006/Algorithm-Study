def diff(p1, p2) :
    if p1 < p2 :
       return p2-p1
    else :
        return p1-p2

def solution(A):
    part = 1
    p1 = sum(A[:1])
    p2 = sum(A[1:])
    min = diff(p1, p2)
    for part, a in zip(range(2, len(A)), A[1:]) :
        p1 += a
        p2 -= a
        temp = diff(p1, p2)
        if temp < min :
            min = temp

    return min
