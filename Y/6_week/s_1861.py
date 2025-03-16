####################
# 1. 맵 순회해주기
# 2. 현재 값에서 깊이 탐색 해주기
#   뎁스 한 번 넘어갈 때 마다 cnt ++
#   한 번 마지막 지점에 갔으면 max_cnt 갱신
#   #
T = int(input())
# delta
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = float('-inf')
    cnt = float('-inf')


    def dfs(cur_r, cur_c, cnt):
        global max_cnt, cnts
        # visited[cur_r][cur_c] = 1
        # cnt += 1
        cnts = cnt

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == graph[cur_r][cur_c] + 1:
                dfs(nr, nc, cnt + 1)


    for i in range(N):
        for j in range(N):
            # cnt = 0
            idx_num = graph[i][j]
            dfs(i, j, 1)

            if max_cnt < cnts:
                max_cnt = cnts
                idx = [i, j]

            elif max_cnt == cnts:
                if graph[i][j] < graph[idx[0]][idx[1]]:
                    idx = [i, j]

    print(f'#{test_case} {graph[idx[0]][idx[1]]} {max_cnt}')