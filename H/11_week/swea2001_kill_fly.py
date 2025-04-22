T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    max_result = 0

    for i in range(N):
        for j in range(N):

            sum = 0
            ei = i + (M-1)
            ej = j + (M-1)

            if ei < N and ej < N:

                for si in range(i, ei+1):
                    for sj in range(j, ej+1):
                        sum += grid[si][sj]

                # for tw in range(N-1):
                #     sum -= grid[i + tw][j + tw]

            if max_result < sum:
                max_result = sum

    print(f'#{tc} {max_result}')