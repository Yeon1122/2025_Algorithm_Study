'''
1.

A : 앞으로
L : 왼 90도
R : 오 90도

델타

상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

X 지점찾기
Y 지점까지 이동.
G를 만나면 이동.
T를 만나면 가만히.

L일때 반시계 (dir+3)%4 >> 회전만함
R일때 시계 (dir+1)%4 >>회전만함
A일때 > dir 방향으로 전진.

dir = 0
R = 0
C = 0

nr = r+dr[dir]
nc = c+dc[dir]

'''
T= int(input())
for tc in range(1, T+1):
    N = int(input())    
    fields = [input() for _ in range(N)]
    Q = int(input())

    C = list(input().split())
    print(C)