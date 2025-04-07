'''
보물섬

[문제이해]
보물섬 지도 - 직사각형 모양
지도 표시: 육지 - L / 바다 - W
이동 가능: 상하좌우 이웃 육지, 같은 곳 중복 불가가
이동 시간: 1칸에 1시간
최단거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두곳에 나뉘어 묻혀있음

[입력]
N, M #보물 지도의 세로의 크기/가로의 크기
tmap #(이중리스트)붙어있는 문자

[출력]
보물이 묻혀있는 두 곳 사이를 최단 거리로 이동하는 시간

[문제풀이]
- 최장거리의 최단시간
- bfs
- 육지에서 시작 cnt 도출
- cnt 갱신하면서 최대 cnt 찾기

1. 같은 출발점 / 같은 도착점인데 더 먼거리로 돌아가서 cnt가 높아요.
=> cnt가 아니라 visited로 풀면 각 위치마다 정확한 시간을 알 수 있음
'''
from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(x,y):
    global result
    visited = [[-1]*M for _ in range(N)]
    visited[x][y] = 0
    q = deque()
    q.append((x,y))

    while q:
        i, j = q.popleft()
        for dir in range(4):
            ni, nj = i+di[dir], j+dj[dir]
            if 0<=ni<N and 0<=nj<M and tmap[ni][nj] == 'L' and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j]+1
                result = max(result, visited[ni][nj])
                q.append((ni,nj))
    
    
N, M = map(int,input().split())
tmap = [list(map(str,input())) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        if tmap[i][j] == 'L':
            bfs(i,j)

print(result)


