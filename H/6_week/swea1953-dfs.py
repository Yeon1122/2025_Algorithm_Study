T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
tunnels = [
    0, 
    [0, 1, 2, 3],
    [0, 1],
    [2, 3],
    [0, 3],
    [1, 3],
    [1, 2],
    [0, 2]
]

def dfs(r, c, hour):
    if hour > L:
        return
    
    visited[r][c] = hour

    tunnel = tunnels[graph[r][c]]
    for dir in tunnel:
        nr = r + dr[dir]
        nc = c + dc[dir]

        if nr < 0 or nr >= N or nc < 0 or nc>= M or graph[nr][nc] == 0:     # 이면 나가라
            continue

        if visited[nr][nc] == 0 or visited[nr][nc] > hour + 1:
            next_dir = -1
            if dir == 0 or dir == 2:
                next_dir = dir + 1
            else:
                next_dir = dir - 1
            if next_dir in tunnels[graph[nr][nc]]:
                dfs(nr, nc, hour+1)

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    answer = N*M        # 맵 사이즈 전부다 초기값으로

    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    dfs(R, C, 1)

    for i in range(N):
        answer -= visited[i].count(0)

    print(f"#{tc} {answer}")