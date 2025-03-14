# 햇수가 가면 빙하가 녹음
#     1. 빙하가 녹는 법칙 - 완탐, != 0 인 것만
#         4방체크 cnt 0 몇갠지
#         빙하 - cnt 
#     2. 갯수 체크 전에 모든 그래프를 돌면서 값 존재하는 좌표값 개수 체크
#     3. 빙하 갯수 세기 : 좌표값 개수랑 (완탐, != 0 인 것에서 출발해서 4방 모두 0 만나면 스탑) 일치 X -> 그때 year 리턴





def melt_glacier(i, j):
    m_cnt = 0
    for i in range(N):
        for j in range(M):
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if map[i][j]:
                    if map[i + dr][j + dc] == 0:
                        m_cnt += 1
            if m_cnt:
                map[i][j] = map[i][j] - m_cnt
    year += 1


def count_glacier(cnt, i, j):
    availables = 0
    global visited

    for i in range(N):
        for j in range(M):
            if map[i][j]:
                availables += 1             # 좌표값 개수

    for i in range(N):
        for j in range(M): 
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]: 
                if map[i][j] and map[i + dr][j + dc]:
                    map[i][j] = map[i + dr][j + dc]


                          

                    visited[i][j] += 1
                    if map[i + dr][j + dc]:
                        map[i][j] = map[i + dr][j + dc]
                    else:
                        cnt += 1
            melt_glacier(i, j)

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
year = 0
result = count_glacier(0, 0, 0)
print(result)

# 1년 지날때마다 빙하 녹이기 bfs
# 빙산 개수는 visited가 0 아닌 수인 곳 가면 처리 dfs -> 이미 처리한 곳 또 가면 빙산이 하나밖에 없는거
# 두개 이상이면 visited 처리한 곳 또 안가게
# 복사는 할 필요 X

# 1년마다 빙산 갯수 체크 -> 2 이상이면 그 햇수 리턴
# 빙하 1년씩 녹이기


