'''
BFS로 확산 시키면 끝

대신 확산이 끝나고 if문으로 검사해야 할 듯

확산 할 때 마다 for문 돌면서 횟수 세어주면 끝

'''
from collections import deque

N, M = map(int,input().split())
tomato_box = [list(map(int,input().split())) for _ in range(M)]
tomato = []

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def ripe_tomato(tomato):
    q = deque()
    for x,y in tomato:
        q.append((x,y))
    step = 0

    while q:
        length_q = len(q)
        for _ in range(len(q)):
            cur_r, cur_c = q.popleft()
            for k in range(4):
                nr = cur_r + dr[k]
                nc = cur_c + dc[k]
                if 0<=nr<M and 0<=nc<N and tomato_box[nr][nc] == 0:
                    tomato_box[nr][nc] = 1
                    q.append((nr,nc))
        step += 1
    for check_tomato in tomato_box:
        if check_tomato.count(0) >= 1:
            return -1

    return step -1





for i in range(M):
    for j in range(N):
        if tomato_box[i][j] == 1:
            tomato.append((i,j))


print(ripe_tomato(tomato))