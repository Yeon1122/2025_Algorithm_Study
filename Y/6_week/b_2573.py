########################
# 0. 1년 카운트를 위해서 무제한 반복. -> while
# 1. 맵을 전체 순회 해줘서 현재 상태의 빙산의 총 넓이 구하기(전체 그래프에서 0이 아닌 값)->forfor
# 2. 맵 순회하면서 0이 아니면 BFS 진행
#   2-1. 빙산 내부에서 자신을 기준으로 상하좌우 탐색, 0인 값이 있으면 visited에 저장,
#        숫자라면 다음 탐색 칸에 넣어주기 (큐에 넣어주기)
#   2-2. 만약 다 돌았다면 (while q가 끝나면) visited면적 구하기(전체 면적-0의 수)
#   2-3. 빙산의 넓이 == visited 면적 -> 빙산 하나임
#        빙산의 넓이 != visited 면적 -> 빙산 하나 아님
#   2-4. 빙산 하나면 년도 +1, 아니면 그대로 현재 년도 내보내주고 반복 멈추기
#   #
from collections import deque


#탐색용 델타
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(i, j):
    global flag, visited_cnt
    visited = [[-1]*C for _ in range(R)]

    q = deque()
    q.append((i, j))
    visited[i][j] += 1

    while q:
        # print(q)
        cur_pos = q.popleft()
        for d in range(len(dc)):
            nr = cur_pos[0]+dr[d]
            nc = cur_pos[1]+dc[d]
            if 0<=nr<R and 0<=nc<C:
                # 2-1.만약 0이면 visited에 더해주기
                if iceberg[nr][nc] == 0:
                    visited[cur_pos[0]][cur_pos[1]] += 1
                    continue
                #숫자라면 다음 탐색 칸에 넣어주기 (큐에 넣어주기)
                if visited[nr][nc] == -1 and iceberg[nr][nc] != 0:
                    visited[nr][nc] += 1
                    q.append((nr, nc))

    for i in range(R):
        for j in range(C):
            if visited[i][j]>=0:
                iceberg[i][j] -= visited[i][j]
                if iceberg[i][j]<0:
                    iceberg[i][j] = 0

    for i in range(R):
        visited_cnt -= visited[i].count(-1)

    if visited_cnt != iceberg_cnt:
        flag = 1

    # print(visited)





R, C = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(R)]
flag = 0
year = -1

while flag == 0:
    # 1.
    iceberg_cnt = R*C
    for i in range(R):
        iceberg_cnt -= iceberg[i].count(0)

# print(iceberg_cnt)
    # 2.
    # br = 0
    no_ice = False
    visited_cnt = R*C
    found = False
    for i in range(R):
        for j in range(C):
            if iceberg[i][j] != 0:
                ci, cj = i, j
                bfs(ci,cj)
                found = True
                break

            if i == R-1 and j == C-1:
                flag = 1
                year = 0
                no_ice = True

        if found:
            break
    if no_ice == False:
        year += 1

    # print('f', flag, visited_cnt, iceberg_cnt)
    # print(year, iceberg)
print(year)