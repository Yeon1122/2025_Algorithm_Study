T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzles = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 가로퍼즐탐색
    for i in range(N):
        cnt = 0
        for d in range(N):
            if puzzles[i][d] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1
    
    # 세로퍼즐탐색
    for j in range(N):
        cnt = 0
        for di in range(N):
            if puzzles[di][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1
        
    print(f'#{tc} {result}')