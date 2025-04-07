from collections import deque

dz = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dx = [0,0,0,0,-1,1]


def spread_tomato(lst):
        global cnt, temp
        cnt = -1
        q = deque(lst)
        while q:
            len_q = len(q)
            for _ in range(len_q):
                z, y, x = q.popleft()
                for dir in range(6):
                    nz, ny, nx = z+dz[dir], y+dy[dir], x+dx[dir]
                    if 0<=nz<H and 0<=ny<N and 0<=nx<M and tomato[nz][ny][nx]==0:
                        tomato[nz][ny][nx] = 1
                        q.append((nz,ny,nx))

            cnt += 1

        for h in range(H):
            for n in range(N):
                for m in range(M):
                    if tomato[h][n][m] == 0:
                        return -1

        return cnt

M, N, H = map(int,input().split())
tomato = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

temp = 0

spread_list = []
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                spread_list.append((h,n,m))
result = spread_tomato(spread_list)
    
print(result)