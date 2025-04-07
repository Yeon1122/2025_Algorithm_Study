'''
미로 탐색

[문제 이해]
N*M크기의 배열로 표현되는 미로
1 - 이동 가능 / 0 - 이동 불가
출발 - (1,1) / 도착 - (N,M)
maze = 출발 - (0,0) / 도착 - (N-1,M-1)
최소의 칸 수 - bfs

[입력]
N, M #배열의 크기 세로, 가로
maze #(이차원 리스트) 붙어있음

[출력]
최소의 칸 수

[문제 풀이]
bfs로 돌면서 해당 칸에 도착하면 결과값 도출
'''

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1 
    cnt = 1

    while q:
        len_q = len(q)
        for _ in range(len_q):
            i, j = q.popleft()

            # if i == N-1 and j == M-1:
            #     return cnt

            for dir in range(4):
                ni, nj = i + di[dir], j + dj[dir]

                if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1 and not visited[ni][nj]:
                    if ni == N-1 and nj == M-1:
                        return cnt+1
                q.append((ni, nj))
                visited[ni][nj] = 1
        cnt += 1



# 입력
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

print(bfs(0, 0))
