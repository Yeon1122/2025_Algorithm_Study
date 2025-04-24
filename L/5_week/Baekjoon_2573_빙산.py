from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        r, c = q.popleft()
        for dir in range(4):
            nr, nc = r+di[dir], c+dj[dir]
            if 0<=nr<N and 0<=nc<M and graph[nr][nc] > 0 and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr,nc))

def melt():
    melt_list = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                k = 0
                for dir in range(4):
                    nr, nc = i+di[dir], j+dj[dir]
                    if 0<=nr<N and 0<=nc<M and graph[nr][nc] == 0:
                        k += 1
                if k > 0:
                    melt_list.append((i, j, k))
    
    for r, c, amount in melt_list:
        graph[r][c] = max(0,graph[r][c] - amount)

def count_dump():
    dump = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i,j)
                dump += 1
    
    return dump
  
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
result = 0

while True:
    visited = [[0]*M for _ in range(N)]
    dump_count = count_dump()

    if dump_count >= 2:
        break

    if dump_count == 0:
        result = 0
        break

    melt()
    result += 1

print(result)