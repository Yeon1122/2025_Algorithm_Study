T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    # 가로 방향 검사
    for i in range(N):
        length = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                length += 1
            else:
                if length == K:
                    cnt += 1
                length = 0
        if length == K:  # 행 끝에 도달한 경우 체크
            cnt += 1

    # 세로 방향 검사
    for j in range(N):
        length = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                length += 1
            else:
                if length == K:
                    cnt += 1
                length = 0
        if length == K:  # 열 끝에 도달한 경우 체크
            cnt += 1

    print(f"#{tc} {cnt}")