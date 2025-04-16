from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def find_air(start_x,start_y,air):
    q=deque()
    q.append((start_x,start_y))
    air[start_x][start_y]=1

    while q:
        x,y=q.popleft()

        for dr in range(4):
            nx=x+dx[dr]
            ny=y+dy[dr]

            if nx<0 or nx>=N or ny<0 or ny>=M or air[nx][ny]:
                continue
            if arr[nx][ny]==1:
                continue
            air[nx][ny]=1
            q.append((nx,ny))

    return air

def solve():
    air=[[0]*M for _ in range(N)]
    find_air(0,0,air)

    for i in range(1,N-1):
        for j in range(1,M-1):
            if arr[i][j]:
                cnt=0
                for dr in range(4):
                    nx=i+dx[dr]
                    ny=j+dy[dr]
                    if air[nx][ny]:
                        cnt+=1
                    if cnt==2:
                        arr[i][j]=0
                        break

N, M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
time=0
while True:
    cheese=sum(lst.count(1) for lst in arr)
    if not cheese:
        break
    
    solve()

    time+=1

print(time)

