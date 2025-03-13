from copy import deepcopy
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solve(x,y):
    global max_go
    for dr in range(4):
        nx = x+dx[dr]
        ny = y+dy[dr]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if arr[nx][ny]==arr[x][y]+1:
            visited[nx][ny]=visited[x][y]+1
            solve(nx,ny)
        else:
            max_go=max(max_go,visited[x][y])
    return max_go

T=int(input())

for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    visited=[[0]*N for _ in range(N)]
    max_value=0
    max_go=0
    for i in range(N):
        for j in range(N):
            copy_v=deepcopy(visited)
            result=solve(i,j)
            if result > max_value:
                max_value=result
                max_idx=arr[i][j]
            visited=copy_v

    print(f"#{tc} {max_idx} {max_value+1}")