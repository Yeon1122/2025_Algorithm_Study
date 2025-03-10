from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]          # 상하좌우 이동
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

def bfs(R, C):
    q = deque([R, C])
    visited[R][C] = 1

    while q:
        r, c = q.popleft()
        dir = tunnels[tunnels[r][c]]
        for i in range(4):
            if dir[i] == 0:
                continue
            next_r, next_c = r + dr[i], c + dc[i]

            if 0 > next_r or next_r >= N or 0 > next_c or next_c >= M:      # 가능범위가 0 <= r < N 이니까 그 반대
                continue
            if visited[next_r][next_c]: # 0이 아니면 이미 지나간거니까 패스스
                continue
            if tunnels[next_r][next_c] == 0:    # 이동불가가
                continue

                



T = int(input())
for tc in range(1, T+1):
    result = 0
    N, M, R, C, L = map(int, input().split())
    origin = [[list(map(int, input().split()))] for _ in range(N)]
    visited = [[0] * M] for _ in range(N)
    bfs(R, C)

    print(f"{tc} {result}")