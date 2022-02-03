def solution(triangle):
    answer = 0
    dp = [[0]+t+[0] for t in triangle]
    for i in range(1,len(triangle)):
        for j in range(1,i+2):
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])
    answer = max(dp[-1])
    return answer