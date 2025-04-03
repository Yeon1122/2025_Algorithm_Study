dz = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dx = [0,0,0,0,-1,1]


def check_tomato(lst):
    count_z = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if lst[h][n][m] == 0:
                    count_z += 1
    
    return count_z

def spread_tomato(z,y,x):
        for dir in range(6):
            nz, ny, nx = z+dz[dir], y+dy[dir], x+dx[dir]
            if 0<=nz<H and 0<=ny<N and 0<=nx<M and tomato[nz][ny][nx]==0:
                tomato[nz][ny][nx] = 1
                spread_list.append((nz,ny,nx))
                

M, N, H = map(int,input().split())
tomato = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

cnt = 0
temp = 0
while True:
    if check_tomato(tomato) == 0:
        result = cnt
        break
    elif temp == check_tomato(tomato):
        result = -1
        break
    else:
        temp = check_tomato(tomato)
        cnt += 1
        spread_list = []
        for h in range(H):
            for n in range(N):
                for m in range(M):
                    if tomato[h][n][m] == 1:
                        spread_tomato(h,n,m)
        
        for a, b, c in spread_list:
            tomato[a][b][c] = 1
        
print(result)