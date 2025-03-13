'''
# 입력데이터
T : tc
N : 방 크기
graph[N][N]
delta

#구조
1로 갈 수 있는 최장거리 탐색한 후 최장이면 시작 지점과 거리 반환
문제

최솟값 일때 이미 min이 들어와서 안됨
1. 원래 값보다 step이 클 때
2. 그 이후에 비교
'''
from collections import deque
def bfs(r,c):
    global mx, min_start
    q = deque()
    q.append((r,c))
    step = 0
    start = graph[r][c]
    while q:
        len_q = len(q)
        for _ in range(len_q):
            cr, cc = q.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == graph[cr][cc] + 1:
                    q.append((nr,nc))
        step += 1
    total = [step, graph[r][c]]

    if step > mx:
        mx = max(step,mx)
        min_start = graph[r][c]
    elif step == mx:
        if start < min_start:
            min_start = min(min_start,start)
    # mx가 기존보다 컸으면 갱신 크거나 같으면 min_start



T = int(input())
dr = [-1,1,0,0]
dc = [0,0,-1,1]
for tc in range(1,1+T):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    # print(graph)
    mx = 0
    min_start = float('inf')
    for i in range(N):
        for j in range(N):
            bfs(i,j)

    print(f'#{tc} {min_start} {mx}')
