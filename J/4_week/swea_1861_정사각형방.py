'''
0. 풀이방안
N^2 방이 N*N형태
1)상하좌우 +1씩 이동 > 상하좌우 세팅해야겠군.
    N-1 인덱스 있다면 좌 / 우로 꺾어줌
2)제일작은값부터 큰값까지 이동, 연속되어야함 

3)같은 최댓값 있다면 제일 작은값

4)이동하는 방 수 = 처음 방 포함 + 이동 방 수
    
1. 입력값
T
N
    N줄 진입
    i, j 2차원배열

상하좌우 이동
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]

dir

nc = dc + dir
nr = dr + dir
    
N-1행까지 가면 꺾어야함
+1 하는 쪽으로 이동해야함.

만약에 이동 최댓값 같으면 더 작은 수 비교해서 채택함.
'''

T = int(input())
number = 0
times = 0

for tc in range(1, T+1):
    N = int(input())
    # rooms = ([0]*N for _ in range(N))            
    graph = [list(map(int, input().split())) for _ in range(N)]

    # print(rooms)
    # for i in range(N):
    #     for j in range(N):

    # print(f'#{tc} {number} {times})