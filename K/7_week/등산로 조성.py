T=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solve(x,y,cnt,chance):
    global max_go
    visited[x][y]=1

    for dr in range(4):
        nx=x+dx[dr]
        ny=y+dy[dr]
        if nx<0 or nx>=N or ny<0 or ny>=N or visited[nx][ny]==1:
            continue
        if arr[nx][ny]<arr[x][y]:
            solve(nx,ny,cnt+1,chance)

        elif arr[nx][ny]-K<arr[x][y] and chance==1:
            for bomb in range(1,K+1):
                backup=arr[nx][ny]
                arr[nx][ny]-=bomb
                if arr[nx][ny]<arr[x][y]:
                    chance=0
                    solve(nx,ny,cnt+1,chance)
                    chance=1
                arr[nx][ny]=backup

        else:
            max_go=max(max_go,cnt)

    visited[x][y]=0

for tc in range(1,T+1):
    N,K=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]

    max_go=1
    max_height = max(map(max, arr))

    for i in range(N):
        for j in range(N):
            if arr[i][j]==max_height:
                visited=[[0]*N for i in range(N)]
                solve(i,j,1,1)
    
    print(f'#{tc} {max_go}')
    