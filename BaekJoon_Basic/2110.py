n, c = map(int, input().split())
array = []
for _ in range(n):
  array.append(int(input()))
array.sort()

start, end = 1, max(array) - min(array)

def check(val):
  now = 1
  tmp = 1
  prev = 0
  while now < n:
    if array[prev] + val <= array[now]:
      tmp += 1
      prev = now
    now += 1
  return tmp

result = 0
while start <= end:
  mid = (start + end) // 2
  if check(mid) >= c:
    result = mid
    start = mid + 1
  else:
    end = mid - 1
print(result)
