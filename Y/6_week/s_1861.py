####################
# 1. 맵 순회해주기
# 2. 현재 값에서 깊이 탐색 해주기
#   뎁스 한 번 넘어갈 때 마다 cnt ++
#   한 번 마지막 지점에 갔으면 max_cnt 갱신
#   #
T = int(input())
#delta
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = float('-inf')
    idx = []


    def dfs(cur_r, cur_c, cnt):
        global max_cnt, idx
        visited[cur_r][cur_c] = 1

        for d in range(4):
            nr = cur_r+dr[d]
            nc = cur_c+dc[d]

            if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0:
                if graph[nr][nc]-1 == graph[cur_r][cur_c] or graph[nr][nc]+1 == graph[cur_r][cur_c]:
                    dfs(nr, nc, cnt+1)

        if cnt>max_cnt:
            if len(idx):
                if graph[idx[0]][idx[1]]>graph[cur_r][cur_c]:
                    idx = [cur_r, cur_c]
                    max_cnt = cnt
            else:
                idx = [cur_r, cur_c]
                max_cnt = cnt

        return cnt

    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            dfs(i, j, 0)

    print(f'#{test_case} {max_cnt} {graph[idx[0]][idx[1]]}')