'''
G : 이동 가능 땅
X : 내 위치
T : 나무 (이동 불가)
Y : 목적지
항상 위를 바라보고 있음

상 우 하 좌


# 입력
T : tc
delta = 상우하좌
N : 그래프 N
graph[N][N]
Q : 조종
dir
for Q 이렇게 움직였을 떄 어떻게 될 것인가 (통과 or 실패)
C, command(A : 이동, L : 왼쪽 90도, R : 오른쪽 90도)

# 구조
직접 옮겨도 되고, 그냥 시뮬레이션만 돌려도 됨.
그냥 시뮬레이션만 돌리면 내 자리로 왔을 때, 문제가 생길 수 있긴 하다.
배열을 따로파서 q로 움직이자


'''
from collections import deque
T = int(input())
dr = [-1,0,1,0]
dc = [0,1,0,-1]
for tc in range(1,T+1):
    N = int(input())
    graph = [list(input()) for _ in range(N)]

    Q = int(input())
    command = []
    for _ in range(Q):
        c, cm = map(str,input().split())
        command.append(cm)
    ground = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'T':
                ground[i][j] = 1
            elif graph[i][j] == 'Y':
                goal = (i,j)
            elif graph[i][j] == 'X':
                start = (i,j)
    result = []

    for com in command:
        RC = start
        dir = 0
        for cm in com:
            if cm == 'R':
                dir = (dir+1)%4
            elif cm == 'L':
                dir = (dir+3)%4
            elif cm == 'A':
                nr, nc = RC[0] + dr[dir], RC[1] + dc[dir]
                if 0 <= nr < N and 0 <= nc < N and ground[nr][nc] != 1:
                    RC = (nr,nc)

        if RC == goal:
            result.append(1)
        else:
            result.append(0)
    print(f'#{tc}', *result)




