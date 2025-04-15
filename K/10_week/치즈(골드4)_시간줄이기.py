from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(start_x,start_y,air):
    q=deque()
    q.append((start_x,start_y))
    visited=[[0]*W for _ in range(H)]
    
    visited[start_x][start_y]=1

    while q:
        x,y=q.popleft()
        for dr in range(4):
            nx=x+dx[dr]
            ny=y+dy[dr]

            if nx<0 or nx>=H or ny<0 or ny>=W or visited[nx][ny]:
                continue
            if arr[nx][ny]==1:
                continue
            visited[nx][ny]=1
            air[nx][ny]=1
            q.append((nx,ny))
    return air

def solve():
    air=[[0]*W for _ in range(H)]
    bfs(0,0,air)

    for i in range(1,H-1):
        for j in range(1,W-1):
            if arr[i][j]:   #치즈일때
                for dr in range(4): #인접한 부분에 공기가 있는지 확인
                    nx=i+dx[dr]
                    ny=j+dy[dr]

                    if air[nx][ny]==1:  #인접한 부분에 공기가 있으면
                        arr[i][j]=0 #해당 치즈를 녹여 없애준다.
                        break

H, W= map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(H)]

last_cheese=0
time=0

while True: 

    cheese=sum(lst.count(1) for lst in arr)
    if not cheese:
        break
    last_cheese=cheese
    solve()
    time+=1 #1시간 추가

print(time)
print(last_cheese)