n = int(input())
array = list(map(int,input().split()))

data = [1]*n

for i in range(n):
  tmp = 0
  for j in range(i):
    if array[i]<array[j]:
      tmp = max(tmp, data[j])
  data[i]+=tmp

print(data)
print(n - max(data))
