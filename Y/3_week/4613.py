T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    ru_list = [input() for _ in range(N)]
    max_cnt = 0

    for i in range(1, N - 1):  # W의 범위
        for j in range(i + 1, N):  # B의 범위
            cnt = 0
            # WBR세주기
            for k in range(i):
                cnt += ru_list[k].count('W')
            for k in range(i, j):
                cnt += ru_list[k].count('B')
            for k in range(j, N):
                cnt += ru_list[k].count('R')

            if cnt > max_cnt:
                max_cnt = cnt

    # 전체 - WBR의 최댓값 => 최소 변경 개수 계산
    result = (N * M) - max_cnt

    print(f'#{test_case} {result}')