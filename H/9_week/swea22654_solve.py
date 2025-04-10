# 방향: 북, 동, 남, 서
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move(C, command, sr, sc, direction):
    r, c = sr, sc
    d = direction

    for i in range(C):
        if command[i] == 'A':
            nr = r + dirs[d][0]
            nc = c + dirs[d][1]
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 'T':
                r, c = nr, nc

        elif command[i] == 'L':
            d = (d - 1) % 4  # 왼쪽 회전

        elif command[i] == 'R':
            d = (d + 1) % 4  # 오른쪽 회전

    return grid[r][c]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = []
    result = []

    for _ in range(N):
        line = input()
        grid.append(list(line))

    # 시작 위치 찾기
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'X':
                sr, sc = i, j
                direction = 0  # 북쪽(위) 바라보는 상태

    Q = int(input())
    for _ in range(Q):
        C, command = input().split()
        C = int(C)
        # 시뮬레이션 실행
        final_cell = move(C, command, sr, sc, direction)
        if final_cell == 'Y':
            result.append(1)
        else:
            result.append(0)

    results = ' '.join(map(str, result))
    print(f'#{tc} {results}')