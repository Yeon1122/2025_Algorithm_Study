###
# M가로 N세로 H높이#

from collections import deque

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
ans = -1
#delta
# dr = []
# dc =
#같은 층 상 우 하 좌 위 아래
tomato_dir = [(-1,0,0), (0,1,0), (1,0,0), (0, -1, 0), (0,0,1), (0,0,-1)]
print(tomato)
#cur_pos[높이][세로][가로]
def bfs(cur_h, cur_r, cur_c):
    cnt = 0
    q = deque()
    q.append((cur_h, cur_r, cur_c))
    while q:
        print(q)
        len_q = len(q)
        cur_pos=q.popleft()
        visited[cur_pos[0]][cur_pos[1]][cur_pos[2]] = 1
        for i in range(len_q):
            for d in range(len(tomato_dir)):
                nh = cur_pos[0]+tomato_dir[d][2]
                nr = cur_pos[1]+tomato_dir[d][1]
                nc = cur_pos[2]+tomato_dir[d][0]

                if 0<=nh<H and 0<=nr<N and 0<=nc<M and tomato[nh][nr][nc] == 0 and not visited[nh][nr][nc]:
                    # tomato[nh][nr][nc] = 1
                    visited[nh][nr][nc] = 1
                    print(visited)
                    q.append((nh, nr, nc))
        cnt += 1
    print(cnt)



#모두 익은게 아닌 경우
flag = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[h][i][j] == 0 and not flag:
                #안 익은 토마토가 있으면 flag = 1
                flag = 1
            #안 익은 토마토가 있어야지 익는게 의미가 있음-> flag==1일떄
            if flag == 1 and tomato[h][i][j] == 1:
                bfs(h, i, j)
if flag != 1:
    ans = 0

print(ans)