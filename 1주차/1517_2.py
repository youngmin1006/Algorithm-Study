import heapq, sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
heap = []

for idx, val in enumerate(line):
    heapq.heappush(heap, (val, idx))

ans = 0
while heap:
    idx, val = heapq.heappop(heap)
    ans += val
print(ans)


