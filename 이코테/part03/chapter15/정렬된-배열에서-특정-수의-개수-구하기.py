from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

left_index = bisect_left(array, x)
right_index = bisect_right(array, x)

if left_index < right_index:
  print(right_index - left_index)
else:
  print(-1)