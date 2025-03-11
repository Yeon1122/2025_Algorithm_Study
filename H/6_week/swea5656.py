from copy import deepcopy
from collections import deque

T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def count_block(graph):
    count = 0
    for i in range(H):
        count += graph[i].count(0)
    
    return H*W-count

def crash_block(start_r, start_c, graph):
    q = deque()
    visited = [[0]*W for _ in range(H)]

    visited[start_r][start_c] = 1
    q.append((start_r, start_c))

    while q:
        r, c = q.popleft()
        for dir in range(4):
            for step in range(1, graph[r][c]):
                nr = r + dr[dir]*step
                nc = c + dc[dir]*step

                if nr < 0 or nr >= H or nc < 0 or nc >= W or graph[nr][nc] == 0 or visited[nr][nc] == 1:
                    continue

                visited[nr][nc] = 1
                q.append((nr, nc))
    
    for r in range(H):
        for c in range(W):
            if visited[r][c] == 1:
                graph[r][c] = 0

    for c in range(W):
        row_idx = H-1
        for r in range(H-1, -1, -1):
            if graph[r][c] == 0:
                continue
            graph[row_idx][c] = graph[r][c]
            row_idx -= 1
        
        for r in range(row_idx, -1, -1):
            graph[r][c] = 0


def perm(cnt, graph):
    global answer

    if cnt == N:
        answer = min(answer, count_block(graph))

        return
    
    for i in range(W):
        row_idx = 0
        while graph[row_idx][i] == 0:
            row_idx += 1
            if row_idx >= H:
                break
        
        if row_idx >= H:
            answer = min(answer, count_block(graph))
            continue

        copy_graph = deepcopy(graph)
        crash_block(row_idx, i, copy_graph)
        perm(cnt+1, copy_graph)


for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]
    answer = float('inf')

    perm(0, graph)

    print(f'#{tc} {answer}')