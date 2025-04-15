T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_result = 0

    if N >= M:
        d = N - M
        # d + 1만큼 돌아보면 됨
        for d in range(d+1):
            result = 0
            for i in range(M):
                result += A[d+i] * B[i]
            if result >= max_result:
                max_result = result
    else:
        d = M - N
        for d in range(d+1):
            result = 0
            for i in range(N):
                result += B[d+i] * A[i]
            if result >= max_result:
                max_result = result

    print(f'#{tc} {max_result}')




    #     for C in range(M, N+1):
    #         for i in range(C):
    #             # 이렇게하면 긴 친구도 영원히 작은 거 갯수만큼의 인덱스만 돎
    #             result += A[i] * B[i]
    #             if result >= max_result:
    #                 max_result = result

            
    # else:
    #     for C in range(N, M+1):
    #         for i in range(C):
    #             result += A[i] * B[i]
    #             if result >= max_result:
    #                 max_result = result
        

