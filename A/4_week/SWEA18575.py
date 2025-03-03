'''
#입력 데이터
T : tc
N : N*N 행렬
graph[N][N]

#구조
각 배열을 돌면서 그 배열의 최대값 최솟값을 구하자.
4방향 델타와 그 곱을 다 더하는거를 해서 구하면 될듯

T
델타

for tc
N
graph
max_sum = float('-inf')
min_sum = float('inf')

for N
    for N
        1. 델타 돌기 for k
            for n 델타의 곱 돌기(크기는 N)
                범위 설정
                더해주는 값

        최댓값 갱신
        최솟값 갱신
'''

T = int(input())
dr = [0,1,0,-1]
dc = [1,0,-1,0]

for tc in range(1,T+1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    max_sum = float('-inf')
    min_sum = float('inf')

    for i in range(N):
        for j in range(N):
            cr = i
            cc = j
            sum = graph[cr][cc]
            for k in range(4):
                for n in range(1,N):
                    nr = cr + dr[k]*n
                    nc = cc + dc[k]*n
                    if 0<=nr<N and 0<=nc<N:
                        sum += graph[nr][nc]
            max_sum = max(max_sum,sum)
            min_sum = min(min_sum,sum)

    print(f'#{tc} {max_sum-min_sum}')







