N,K = map(int,input().split())
ob = [list(map(int,input().split())) for _ in range(N)]
ob.insert(0,[0,0])

knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        weight = ob[i][0]
        val = ob[i][1]

        if j< weight:#버틸수 있는 무게를 넘으면 그 전꺼 그대로 가져옴
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(val+knapsack[i-1][j-weight],knapsack[i-1][j])

print(knapsack[N][K])