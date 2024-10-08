import heapq

n = int(input())
hq = []
for _ in range(n):
  heapq.heappush(hq,int(input()))
ans = 0
while -1:
  if len(hq)<2: break
  tmp = heapq.heappop(hq) + heapq.heappop(hq)
  ans+=(tmp)
  heapq.heappush(hq, tmp)
print(ans)
