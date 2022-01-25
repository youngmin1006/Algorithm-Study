n,w,L = map(int,input().split())
weights = list(map(int,input().split()))

q = [0]*w
sec = 0

while q:
    # print(q)
    sec+=1
    q.pop(0)
    if weights:
        if sum(q)+weights[0] <=L :# 트럭을 올려도 무게가 넘지 않으면
            q.append(weights.pop(0))
        else: #무게가 넘으면
            q.append(0)

print(sec)


