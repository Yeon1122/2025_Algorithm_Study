from collections import deque
dx=[-1,0,1,0]
dy=[0,-1,0,1]

def solve(start_x,start_y,C,Crr):
    q=deque()
    q.append((start_x,start_y,0))
    view=0

    while q:
        x,y,doit=q.popleft()
        visited[x][y]=1
        if doit==C:
            result.append(0)
            return
        if Crr[doit]=='A': 
            for dr in range(4):
                if dr == view:
                    nx=x+dx[dr]
                    ny=y+dy[dr]

                    if nx>=N or nx<0 or ny>=N or ny<0 or visited[nx][ny]:
                        continue
                    if arr[nx][ny]=='T':
                        continue
                    if arr[nx][ny]=='Y':
                        result.append(1)
                        return
                    q.append((nx,ny,doit+1))
                    break
        elif doit=='L':
            if view==3:
                view=0
            else:
                view+=1

        elif doit=='R':
            if view==0:
                view=3
            else:
                view-=1

        q.append((nx,ny,doit+1))


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[input() for _ in range(N)]
    Q=int(input())
    result=[]

    start_find=False
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='X':
                start_x,start_y=i,j
                start_find=True
                break
        if start_find:
            break

    for _ in range(Q):
        C,Crr=map(str,input().split())
        C=int(C)
        visited=[[0]*N for _ in range(N)]
        solve(start_x,start_y,C,Crr)

    print(f'{tc} {result}')