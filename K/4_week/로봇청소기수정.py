dx=[-1,0,1,0]
dy=[0,1,0,-1]

N, M=map(int,input().split())
r, c, d=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
count=0

def clean(x,y,d):
    global count
    if arr[x][y]==0:
        arr[x][y]=2 #현재 칸을 청소한다.
        count+=1
    view=d
    
    for i in range(4):
        view=(d+3-i)%4
        nx,ny=x+dx[view],y+dy[view]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if arr[nx][ny]==0:
            clean(nx,ny,view)
            return

    back_x,back_y=x-dx[d],y-dy[d]   #후진~
    if 0<=back_x<N and 0<=back_y<M:
        if arr[back_x][back_y]!=1:  #후진한곳이 벽이 아니면 실행
            clean(back_x,back_y,d)



clean(r,c,d)
print(count)
