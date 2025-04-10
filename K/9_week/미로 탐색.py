from collections import deque

dx=[-1,1,0,0]
dy = [0,0,-1,1]

def dfs(startx,starty):
    q=deque()
    q.append((startx,starty))
    visited=[[0]*M for _ in range(N)]
    visited[0][0]=1
    while q:
        x,y=q.popleft()

        for dr in range(4):
            nx=x+dx[dr]
            ny=y+dy[dr]

            if nx<0 or nx>=N or ny <0 or ny>=M or visited[nx][ny]:
                continue
            if arr[nx][ny]==0:
                continue
            visited[nx][ny]=visited[x][y]+1
            q.append((nx,ny))
    
    return visited[N-1][M-1]


N, M= map(int,input().split())
arr=[list(map(int,input())) for _ in range(N)]

print(dfs(0,0))