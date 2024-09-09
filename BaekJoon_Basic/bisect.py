from bisect import bisect_left, bisect_right

# Solution ver1.
n, m = map(int, input().split())
data = list(map(int, input().split()))

result = bisect_right(data, m) - bisect_left(data, m)
if result == 0: result = -1
print(result)

# Solution ver2.
result_left, result_right = -1, -1
start, end = 0, n - 1
while start <= end:
  mid = (start + end) // 2
  if data[mid] == m:
    result_left = mid
    end = mid - 1
  elif data[mid] > m:
    end = mid - 1
  else:
    start = mid + 1

start, end = 0, n - 1
while start <= end:
  mid = (start + end) // 2
  if data[mid] == m:
    result_right = mid
    start = mid + 1
  elif data[mid] > m:
    end = mid - 1
  else:
    start = mid + 1
if result_left == -1: print(-1)
elif result_left == result_right: print(1)
else:
  print(result_right, result_left)
  print(result_right - result_left + 1)
