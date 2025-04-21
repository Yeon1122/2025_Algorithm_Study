dx=[-1,0,1,0]   #상 우 하 좌
dy=[0,1,0,-1]
dr=1

N=int(input())
K=int(input())
apple_position=[]
for _ in range(K):
    x,y=map(int,input().split())
    x-=1
    y-=1
    apple_position.append((x,y))
L=int(input())
time=[] #방향전환명령 시간
dr_command=[]   #방향전환명령
snake=[]

for _ in range(L):
    t, c=map(str,input().split())
    t=int(t)+1
    time.append(t)
    dr_command.append(c)

t=1
x=y=0
while True:

    snake.append((x,y))   #뱀의 머리 안착

    if t in time:
        change_dr=dr_command[time.index(t)]
        if change_dr=='L':
            dr=(dr+3)%4
        elif change_dr=='D':
            dr=(dr+1)%4

    nx=x+dx[dr]
    ny=y+dy[dr]

    if (nx<0 or nx>=N or ny<0 or ny>=N) or (nx,ny) in snake:    #다음위치가 벽이거나 뱀의 몸이면
        break
    if (nx,ny) in apple_position:   #다음위치에 사과가 있으면
        apple_position.remove((nx,ny))  #사과먹기
    else:
        snake.pop(0)    #사과가 없으면 꼬리가 위치한 칸을 비운다

    x=nx
    y=ny
    t+=1

print(t)

