T=int(input())
dx=[0,0,1,-1]   #좌우상하
dy=[1,-1,0,0]   #좌우상하
views='<>^v'
def bomb(x,y,view):
    bombx,bomby=x,y
    for i in range(4):
        if i == view:

            while True:
                nx,ny=bombx+dx[i], bomby+dy[i]
                if nx<0 or nx>=H or ny<0 or ny>=W:
                    break
                if arr[nx][ny]=='*':    #벽돌
                    arr[nx][ny]='.' #평지로 바꾸기
                if arr[nx][ny]=='#':    #강철
                    break

for tc in range(1,T+1):
    H, W=map(int,input().split())
    arr=[input() for _ in range(H)]
    N=int(input())
    arr_N=input()

    view=0  #바라보는 방향

    for i in range(H):
        for j in range(W):
            if arr[i][j] in '^v<>':
                x,y=i,j
                if arr[i][j]=='<':
                    view=0
                if arr[i][j]=='>':
                    view=1
                if arr[i][j]=='^':
                    view=2
                if arr[i][j]=='v':
                    view=3
                break

    for doit in arr_N:
        if doit=='L':
            nx,ny=x+dx[0], y+dy[0]
            if nx<0 or nx>=H or ny<0 or ny>=H:
                break
            if arr[nx][ny]=='-':
                break
            x,y=nx,ny
            view=0

        if doit=='R':
            nx,ny=x+dx[1], y+dy[1]
            if nx<0 or nx>=H or ny<0 or ny>=H:
                break
            if arr[nx][ny]=='-':
                break
            x,y=nx,ny
            view=1

        if doit=='U':
            nx,ny=x+dx[2], y+dy[2]
            if nx<0 or nx>=H or ny<0 or ny>=H:
                break
            if arr[nx][ny]=='-':
                break
            x,y=nx,ny
            view=2

        if doit=='D':
            nx,ny=x+dx[3], y+dy[3]
            if nx<0 or nx>=H or ny<0 or ny>=H:
                break
            if arr[nx][ny]=='-':
                break
            x,y=nx,ny
            view=3

        if doit =='S':  
            bomb(x,y,view)
    
    for i in range(4):
        if i==view:
            arr[x][y]=views[i]
            
    print(f'#{tc}',end=' ')
    for i in range(H):
        print(arr[i])

