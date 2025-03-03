'''
#입력 데이터
T : tc
N,M :
Ai
Bj
max_sum = ('-inf')

#구조
N과 M 크기 비교 후
각각의 인덱스를 곱해주면 되는데 짧은 쪽이 움직여야 함.
        3 5 1
for i (N-M+1)
    sum = 0
    for j in range(짧은 얘)
        sum += Ai[i+j] * Bi[i+j]

    mas_sum = max(max_sum,sum)

'''

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    max_sum = float('-inf')

    if N > M:
        for i in range(abs(N-M)+1):
            sum = 0
            for j in range(M):
                sum += Ai[i+j] * Bi[j]
            max_sum = max(max_sum,sum)

    elif N < M:
        for i in range(abs(N - M)+1):
            sum = 0
            for j in range(N):
                sum += Ai[j] * Bi[i + j]
            max_sum = max(max_sum, sum)

    else: # 두 개 같을 때
        sum = 0
        for i in range(N):
            sum = Ai[i] * Bi[i]
        max_sum = max(max_sum,sum)

    print(f'#{tc} {max_sum}')


