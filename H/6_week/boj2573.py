from collections import deque

def melt_glacier():
    global glacier_map
    melting = [[0] * M for _ in range(N)]  

    for i in range(N):
        for j in range(M):
            if glacier_map[i][j] > 0:
                cnt = 0
                for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < N and 0 <= nj < M and glacier_map[ni][nj] == 0:
                        cnt += 1
                melting[i][j] = cnt

    for i in range(N):
        for j in range(M):
            if glacier_map[i][j] > 0:
                glacier_map[i][j] = max(0, glacier_map[i][j] - melting[i][j])

def bfs(i, j, visited):
    queue = deque([(i, j)])
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ni, nj = x + dr, y + dc
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and glacier_map[ni][nj] > 0:
                visited[ni][nj] = True
                queue.append((ni, nj))

def count_glacier():
    component_count = 0
    visited = [[False] * M for _ in range(N)]
    has_ice = False 

    for i in range(N):
        for j in range(M):
            if glacier_map[i][j] > 0:
                has_ice = True 
                if not visited[i][j]:
                    bfs(i, j, visited)
                    component_count += 1

    return component_count, has_ice

N, M = map(int, input().split())
glacier_map = [list(map(int, input().split())) for _ in range(N)]
year = 0

while True:
    melt_glacier()
    year += 1
    component_count, has_ice = count_glacier()

    if component_count > 1:
        print(year)
        break
    if not has_ice:
        print(0)
        break