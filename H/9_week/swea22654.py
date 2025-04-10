lr = [-1, 1, 0, 0]
lc = [0, 0, -1, 1]
# 상하좌우

def move(C, command, sr, sc, dr, dc):
    for i in range(C):
        if command[i] == 'A':
            if 0 <= sr-1 <= N-1 and grid[sr-1][sc] != 'T':
                sr = sr - 1

        if command[i] == 'L':
            if dr == -1 and dc == 0 or dr == 0 and dc == -1:
                dr += 1
                dc -= 1
            if dr == 1 and dc == 0:
                dr -= 1
                dc += 1
            if dr == 0 and dc == 1:
                dr -= 1
                dc -= 1

        if command[i] == 'R':
            if dr == -1 and dc == 0:
                dr += 1
                dc += 1
            if dr == 0 and dc == -1:
                dr -= 1
                dc += 1
            if dr == 1 and dc == 0:
                dr -= 1
                dc -= 1
            if dr == 0 and dc == 1:
                dr += 1
                dc -= 1

    return grid[sr][sc]

            
# -1, 0		0, -1		+1 -1
# 0, -1		1, 0		+1 -1
# 1, 0		0, 1		-1 +1
# 0, 1		-1, 0		-1 -1

# -1, 0		0, 1		+1 +1
# 0, -1		-1, 0		-1 +1
# 1, 0		0, -1		-1 -1
# 0, 1		1, 0		+1 -1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = []
    result = []
    for _ in range(5):      # map 입력
        line = input()  
        grid.append(list(line))
    for j in range(N):
        for i in range(N):
            if grid[i][j] == 'X':    # 시작위치 찾기
                sr = i
                sc = j
                dr = -1             # 바라보는 기본 방향 세팅
                dc = 0

    Q = int(input())
    for _ in range(Q):
        C, command = input().split()
        C = int(C)
        if move(C, command, sr, sc, dr, dc) == 'Y':
            result.append(1)
        else:
            result.append(0)
    results = ' '.join(map(str, result))
    print(f'#{tc} {results}')