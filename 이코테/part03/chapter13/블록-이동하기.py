from collections import deque

def bfs(x, y, board):
    answer = 0
    n = len(board)

    # 우, 하 먼저 탐색
    # 우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    d = 2 # default: 좌
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if board[x][y] == 0:
            board[x][y] = -1
            board[x + dx[d]][y + dy[d]] = -1
            # 상하좌우 중 갈 수 있는 칸 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 지도를 벗어나면
                if nx < 0 or nx + dx[d] < 0 or ny < 0 or ny + dy[d] < 0 or nx >= n or nx + dx[d] >= n or ny >= n or ny + dy[d] >= n:
                    continue
                # 벽이면
                if board[nx][ny] == 1 or board[nx + dx[d]][ny + dy[d]] == 1:
                    continue
                # 이미 방문한 곳이면 회전
                if board[nx][ny] == -1 or board[nx + dx[d]][ny + dy[d]] == -1:
                    if i == 1 or i == 3:
                        # 로봇이 90도 회전할 때 1초
                        answer += 1
                        nx = max(nx, nx + dx[d])
                        ny = max(ny, ny + dy[d])
                        queue.append((nx, ny))
                        d = (d+1) % 4
                    else:
                        continue
                # 처음 방문한 곳이면
                if board[nx][ny] == 0:
                    # 로봇이 한 칸 이동할 때 1초
                    answer += 1
                    queue.append((nx, ny))
    return answer

def solution(board):
    # 지도를 탐색하며 현재 위치 업데이트
    # 시간 복잡도 : O(N^2) = O(10,000)
    # 로봇이 (N, N) 위치일 때 필요한 최소 시간을 return
    return bfs(0, 1, board)

board = [[0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]
print(solution(board))