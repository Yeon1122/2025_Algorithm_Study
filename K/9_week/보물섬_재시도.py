from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(s_x,s_y):
    global max_distance

    q=deque()
    q.append((s_x,s_y))
    visited=[[0]*W for _ in range(H)]
    visited[s_x][s_y]=1
    
    while q:
        x,y=q.popleft()
        for dr in range(4):
            nx= x+dx[dr]
            ny= y+dy[dr]

            if nx>=H or nx<0 or ny>=W or ny<0 or arr[nx][ny]=='W':
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny]=visited[x][y]+1
            if arr[nx][ny]=='L':
                max_distance=max(max_distance,visited[nx][ny]-1)
            q.append((nx,ny))
    return 0

H, W=map(int,input().split())
arr=[input() for _ in range(H)]
max_distance=0
for i in range(H):
    for j in range(W):
        if arr[i][j]=='L':
            bfs(i,j)

print(max_distance)