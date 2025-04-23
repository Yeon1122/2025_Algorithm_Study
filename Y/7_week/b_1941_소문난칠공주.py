import pprint
from collections import deque

N = 5 #자리 가로세로
K = 7 #7공주
seat = [list(input()) for _ in range(N)]
#delta
dr = [-1,0,1,0]
dc = [0,1,0,-1]
seat_idx = []
y_seat = []
comb_seat = []
princess = [] #경우의 수들, ans = len(princess)

#자리 조합을 만들고 dfs 진행 -> 연속된 자리가 7개면 princess에 append


ans_count = 0

def bfs(cur_rc):
    global ans_count
    visited = [0] * 7
    visited_idx = comb_seat.index(cur_rc)
    visited[visited_idx] = 1
    q=deque()
    q.append(cur_rc)
    cnt = 1

    while q:
        cur_pos = q.popleft()
        for d in range(len(dr)):
            nr = cur_pos[0] + dr[d]
            nc = cur_pos[1] + dc[d]
            if 0<=nr<N and 0<=nc<N and (nr, nc) in comb_seat and not visited[comb_seat.index((nr, nc))]:
                cnt += 1
                visited[comb_seat.index((nr, nc))] = 1
                q.append((nr, nc))

                # print(visited, cnt)
                if cnt == 7:
                    ans_count += 1

y=0
def comb(cnt, idx):
    global y
    # print(y, comb_seat)

    #조합 가지치기()
    if cnt >= 4:
        y = 0
        for i in comb_seat:
            if i in y_seat:
                y += 1
            if y>=4:
                return

    #가지치고 남은 조합
    if cnt == 7:
        # print(comb_seat)
        bfs(comb_seat[0])
        return


    for i in range(idx, len(seat_idx)):
        comb_seat.append(seat_idx[i])
        comb(cnt+1, i+1)
        comb_seat.pop()



for i in range(N):
    for j in range(N):
        seat_idx.append((i, j))
        if seat[i][j] == 'Y':
            y_seat.append((i, j))


comb(0, 0)

print(ans_count)