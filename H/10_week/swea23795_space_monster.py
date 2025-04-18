T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 새로운 맵을 만들어서, 광선 닿은 곳 표시
    laser = [[0]*N for _ in range(N)]  # 0: 안전, 1: 위험
    
    # 괴물 위치 찾기
    monsters = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                monsters.append((i, j))
    
    # 각 괴물마다 광선 쏘기
    for i, j in monsters:
        for dir in range(4):  # 4방향
            ni, nj = i, j
            while True:
                ni += di[dir]
                nj += dj[dir]
                # 맵 벗어나면 멈춤
                if not (0 <= ni < N and 0 <= nj < N):
                    break
                # 벽 만나면 멈춤
                if grid[ni][nj] == 1:
                    break
                # 빈칸(0)이라면, 위험 표시
                laser[ni][nj] = 1
    
    # 안전한 빈칸 개수 세기
    safe_count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0 and laser[i][j] == 0:
                safe_count += 1
    
    print(f"#{tc} {safe_count}")
