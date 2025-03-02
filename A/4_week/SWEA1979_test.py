'''
#입력 데이터
T : tc
N : 가로 세로
단어의 길이 K


구조
T 입력
N, K 입력
graph[N][N]

연속 된 1을 찾으면서, K개수 만큼 1인 곳을 찾으면 cnt
for N
    cnt = 0
    for N
        graph == 1

        graph == 0
            cnt 값이 K와 같은지 확인 후
            cnt 초기화
    끝난 경우 cnt K 같은 지 확인



'''

T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if graph[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:  # 0을 만났을 때 정확히 K개라면 카운트
                    ans += 1
                cnt = 0  # 리셋
        if cnt == K:
            ans += 1
    for i in range(N):
        cnt = 0
        for j in range(N):
            if graph[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:  # 0을 만났을 때 정확히 K개라면 카운트
                    ans += 1
                cnt = 0  # 리셋
        if cnt == K:
            ans += 1
    print(f'#{tc} {ans}')