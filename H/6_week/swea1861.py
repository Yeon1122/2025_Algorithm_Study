def moving_room(i, j):
    if i == 0 or j == 0 or i == N-1 or j == N-1:
        return

    elif map[i][j] == 0 and 0 < i < N-1 and 0 < j < N-1:
        global max_cnt, value_max
        value_max = map[i][j]
        max_cnt = cnt

    else:   
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 < i + dr < N-1 and 0 < j + dc < N-1 and map[i + dr][j + dc] == True and map[i + dr][j + dc] == map[i][j] + 1:
                cnt += 1
                map[i][j] = map[i + dr][j + dc]
                moving_room()

T = int(input())
for tc in range(1, T+1):
    result = 0
    value_max = 0
    max_cnt = 0
    cnt = 0
    c = []
    N = int(input())
    map = [list(map(int, input().split())) for _ in range(N)]
    print(map)
    for i in range(N):
        for j in range(N):
            moving_room(i, j)
    if max_cnt != 0:
        c += max(max_cnt)
        if len(c) == 1:
            result = original_c, c
        else:
            min()

    print(f"{tc} {result}")