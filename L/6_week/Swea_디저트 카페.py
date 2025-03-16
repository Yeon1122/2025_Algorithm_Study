di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
 

def move(r, c, dir, cnt, visited):
    global result
 
    if dir == 3 and r == start_r and c == start_c:
        result = max(cnt, result)
        return
    
    for d in range(2):
        dir += d

        if dir > 3:
            return
 
        nr, nc = r + di[dir], c + dj[dir]

        if 0 <= nr < N and 0 <= nc < N and not visited[graph[nr][nc]]:
            visited[graph[nr][nc]] = 1
            move(nr, nc, dir, cnt+1, visited)
            visited[graph[nr][nc]] = 0
 

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    visited = [0] * 101
    for i in range(N):
        for j in range(N):
            start_r, start_c = i, j
            move(i, j, 0, 0, visited)
    print(f"#{tc} {result}")