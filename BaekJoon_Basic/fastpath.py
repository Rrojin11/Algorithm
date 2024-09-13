INF = int(1e9)

n,m = map(int,input().split())
data = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
  a,b = map(int,input().split())
  data[a][b] = 1

for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j: 
      data[i][j] = 0


for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      data[a][b] = min(data[a][b], data[a][k]+data[k][b])

result = 0
for i in range(1,n+1):
  tmp = sum(data[i])
  if tmp>INF:
    pass
  else:
    result+=1
print(data)
print(result)
