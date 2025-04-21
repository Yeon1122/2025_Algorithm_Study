from collections import deque
from copy import deepcopy

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(start_x,start_y):
    global moved
    q=deque()
    q.append((start_x,start_y))
    group=set()
    group.add((start_x,start_y))
    visited.add((start_x,start_y))

    while q:
        x,y=q.popleft()

        for dr in range(4):
            nx= x+dx[dr]
            ny= y+dy[dr]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if (nx,ny) in visited:
                continue
            if L<=abs(arr[x][y]-arr[nx][ny])<=R:    #인접한 곳이 L이상 R이하면
                visited.add((nx,ny))    #방문체크
                group.add((nx,ny))  #연합에 추가

                q.append((nx,ny))

    if len(group)>=2:
        moved=True
    average=sum(arr[gx][gy] for gx,gy in group)//len(group) #연합안의 인구수 평균 구해서
    for gx,gy in group: #인구 이동
        arr[gx][gy]=average

def is_possible(x, y):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                return True
    return False

N, L, R=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
day=0
moved=False

while True:
    # backup=deepcopy(arr)
    moved=False
    visited=set()
    for i in range(N):
        for j in range(N):
            possible=is_possible(i,j)
            if (i,j) not in visited and possible:    #방문체크를 한 적이 없으면
                bfs(i,j)

    if not moved:
        break
    day+=1

print(day)