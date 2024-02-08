def binarySearch(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    # 중간점이 target과 같으면 mid return
    if array[mid] == target:
      return mid
    # 중간점이 target보다 작으면
    elif array[mid] < target:
      start = mid + 1
    # 중간점이 target보다 크면
    else:
      end = mid - 1
  # start가 end보다 크면 target이 없는 것이므로 None return
  return None

n, target = map(int, input().split())
array = list(map(int, input().split()))

answer = binarySearch(array, target, 0, n-1)
if answer is None:
  print("원소가 존재하지 않습니다.")
else:
  print(answer + 1)