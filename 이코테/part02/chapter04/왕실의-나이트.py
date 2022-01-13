# 나이트의 위치 location 저장
location = input()

# location을 row와 col로 분리
col = location[0]
row = location[1]

# rows와 cols 선언
cols = "abcdefgh"
rows = "12345678"

# 나이트가 이동할 수 있는 경우의 수 cnt 선언
cnt = 0

# rowIndex와 colIndex 찾기
colIndex = cols.index(col)
rowIndex = rows.index(row)

# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
# 왼쪽으로 2번
newColIndex = colIndex - 2
if newColIndex >= 0:
  ## 위로 1 번
  newRowIndex = rowIndex - 1
  if newRowIndex >= 0:
    cnt += 1
  ## 아래로 1번
  newRowIndex = rowIndex + 1
  if newRowIndex < len(rows):
    cnt += 1

# 오른쪽으로 2번
newColIndex = colIndex + 2
if newColIndex < len(cols):
  ## 위로 1번
  newRowIndex = rowIndex - 1
  if newRowIndex >= 0:
    cnt += 1
  ## 아래로 1번
  newRowIndex = rowIndex + 1
  if newRowIndex < len(rows):
    cnt += 1

# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
# 위로 2번
newRowIndex = rowIndex - 2
if newRowIndex >= 0:
  ## 왼쪽으로 1 번
  newColIndex = colIndex - 1
  if newColIndex >= 0:
    cnt += 1
  ## 오른쪽으로 1번
  newColIndex = colIndex + 1
  if newColIndex < len(cols):
    cnt += 1

# 아래로 2번
newRowIndex = rowIndex + 2
if newRowIndex < len(rows):
  ## 왼쪽으로 1 번
  newColIndex = colIndex - 1
  if newColIndex >= 0:
    cnt += 1
  ## 오른쪽으로 1번
  newColIndex = colIndex + 1
  if newColIndex < len(cols):
    cnt += 1

# cnt 출력
print(cnt)