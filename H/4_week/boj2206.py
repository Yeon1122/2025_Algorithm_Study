from collections import deque

# 입력 받기
N, M = map(int, input().split())  # N: 행(row) 개수, M: 열(column) 개수
origin_map = [list(map(int, input().strip())) for _ in range(N)]  # 2차원 리스트로 변환하여 저장

# 방향 벡터 (상, 하, 좌, 우) → (row 변화, column 변화)
dr = [-1, 1, 0, 0]  # 행(row) 변화 (위로 이동, 아래로 이동)
dc = [0, 0, -1, 1]  # 열(column) 변화 (왼쪽으로 이동, 오른쪽으로 이동)

# BFS(너비 우선 탐색) 구현
def bfs():
    queue = deque()
    queue.append((0, 0, 0))  # 시작 위치 (row, column, 부순 벽 개수)
    
    # 방문 배열 (2개를 사용하여 벽을 부쉈을 때와 부수지 않았을 때를 구분)
    visited = [[[float('inf')] * M for _ in range(N)] for _ in range(2)]
    
    # 시작 지점 방문 처리 (벽을 부수지 않은 상태에서 시작)
    visited[0][0][0] = 0  

    while queue:
        r, c, wall_count = queue.popleft()  # 현재 위치 (r, c)와 부순 벽 개수 (wall_count)

        # 목적지에 도착하면 최단 거리 반환
        if r == N - 1 and c == M - 1:
            return visited[wall_count][r][c] + 1  # 시작 지점을 0으로 설정했으므로 +1

        # 네 방향(상, 하, 좌, 우)으로 이동 시도
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]  # 이동할 위치 (새로운 row, column)

            # 지도 범위를 벗어나지 않는 경우에만 검사
            if 0 <= nr < N and 0 <= nc < M:
                
                # 벽이 없는 경우 (이동 가능)
                if origin_map[nr][nc] == 0 and visited[wall_count][nr][nc] == float('inf'):
                    visited[wall_count][nr][nc] = visited[wall_count][r][c] + 1  # 거리 갱신
                    queue.append((nr, nc, wall_count))  # 이동한 좌표를 큐에 추가
                
                # 벽이 있는 경우 (한 개까지 부술 수 있음)
                elif origin_map[nr][nc] == 1 and wall_count == 0 and visited[1][nr][nc] == float('inf'):
                    visited[1][nr][nc] = visited[0][r][c] + 1  # 벽을 부수고 이동한 거리 갱신
                    queue.append((nr, nc, 1))  # 벽을 부쉈으므로 wall_count=1로 이동

    return -1  # 목적지에 도달할 수 없는 경우 -1 반환

# 결과 출력
print(bfs())