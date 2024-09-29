import heapq
INF = int(1e9)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

n = int(input())
data = []

for _ in range(n):
  data.append(list(map(int,input().split())))

q = []
q.append((data[0][0], 0,0))

while q:
  dist, x,y = heapq.heappop(q)
  if x==n-1 and y==n-1:
    print(dist)
    break
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx>=0 and nx<n and ny>=0 and ny<n:
      cost = data[nx][ny] + dist
      data[nx][ny] = cost
      heapq.heappush(q, (cost, nx,ny))
