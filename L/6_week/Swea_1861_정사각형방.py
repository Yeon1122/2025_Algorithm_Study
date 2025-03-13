di = [-1,1,0,0]
dj = [0,0,-1,1]

def dfs(r,c):
    global temp_dis
    for dir in range(4):
        nr, nc = r+di[dir], c+dj[dir]
        if 0<=nr<N and 0<=nc<N and graph[nr][nc] == graph[r][c] + 1: #not visited[nr][nc]
            # visited[nr][nc] = 1
            temp_dis += 1
            dfs(nr,nc)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    result_num = float('-inf')
    result_dis = float('-inf')

    for i in range(N):
        for j in range(N):
            temp_num = graph[i][j]
            temp_dis = 1
            # visited = [[0]*N for _ in range(N)]
            # visited[i][j] = 1
            dfs(i, j)
            if result_dis < temp_dis:
                result_dis = temp_dis
                result_num = temp_num
            elif result_dis == temp_dis:
                if result_num > temp_num:
                    result_num = temp_num
    
    print(f'#{tc} {result_num} {result_dis}')
