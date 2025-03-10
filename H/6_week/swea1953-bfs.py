import sys
sys.stdin = open("input.txt", "r")
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

def bfs(R, C):
    dq = deque([(R, C)])    
    visited[R][C] = 1 

    while dq:
        nowy, nowx = dq.popleft()
        dirs = types[graph[nowy][nowx]]

        for i in range(4):      
            if dirs[i] == 0:
                continue

            new_y = nowy + dy[i]
            new_x = nowx + dx[i]

            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue

            if visited[new_y][new_x]:
                continue

            if graph[new_y][new_x] == 0:
                continue

            next_dirs = types[graph[new_y][new_x]]

            if i % 2 == 0 and next_dirs[i + 1] == 0:
                continue

            if i % 2 == 1 and next_dirs[i - 1] == 0:
                continue

            if visited[nowy][nowx] + 1 > L:
                continue

            visited[new_y][new_x] = visited[nowy][nowx] + 1
            dq.append((new_y, new_x))

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')