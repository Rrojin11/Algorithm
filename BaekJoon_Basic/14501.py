n = int(input())
ts,ps = [0],[0]

for _ in range(n):
  t,p = map(int,input().split())
  ts.append(t)
  ps.append(p)


for i in range(1,n+1):
  if ts[i]+i>n+1:
    ps[i]=0

for i in range(1,n+1):
  tmp = 0
  for j in range(1,i):
    if ts[j]+j<=i:
      tmp = max(tmp, ps[j])
  ps[i] +=tmp

print(ps)
print(max(ps))
