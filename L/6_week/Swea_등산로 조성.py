di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def find_route(r, c, cnt, flag):
    global max_distance
    
    for dir in range(4):
        ni, nj = r + di[dir], c + dj[dir]
        
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        
        if graph[r][c] > graph[ni][nj]:
            find_route(ni,nj,cnt+1,flag)
        elif graph[ni][nj]-K<graph[r][c] and flag == 1:
            for k in range(1,K+1):
                temp = graph[ni][nj]
                if graph[ni][nj]-k > 0:
                    graph[ni][nj] -= k
                    if graph[r][c] > graph[ni][nj]:
                        chance = 0
                        find_route(ni,nj,cnt+1,flag)
                        chance = 1
                    graph[ni][nj] = temp
        else:
            max_distance = max(max_distance,cnt)

    return max_distance

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split()) 
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    max_height = max(max(row) for row in graph) 
    result = float("-inf")
    max_distance = 1

    for i in range(N):
        for j in range(N):
            if graph[i][j] == max_height:
                result = max(result, find_route(i,j,1,1))

    print(f'#{tc} {result}')
