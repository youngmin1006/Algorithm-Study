from itertools import combinations
from itertools import permutations

N =  int(input())
num =  list(range(N))
S = []
for i in range(N):
    S.append(list(map(int,input().split())))

#team_s = [0 for i in range(N/2)]

def solve():
    temp_s = list(combinations(num,int(N/2)))#1,2,3
    min_val = int(1e9)
    for team_s in temp_s:#start 팀 하나하나
        team_l = list(set(num) - set(team_s))
        list(team_s)
        s_total = 0
        l_total = 0
        s_per = list(permutations(team_s,2))
        l_per = list(permutations(team_l, 2))
        for i in s_per:
            s_total+=S[i[0]][i[1]]
        for i in l_per:
            l_total+=S[i[0]][i[1]]
        min_val = min(min_val,abs(s_total-l_total))
    print(min_val)

solve()
