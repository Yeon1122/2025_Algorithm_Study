T = int(input())

for tc in range(1, T+1):
    N = int(input())
    map1 = [list(map(int, input().split())) for _ in range(N)]

    max_sum = float('-inf')
    min_sum = float('inf')

    for i in range(N):
        for j in range(N):
            sum = 0
            if map1[i][j] or map1[i][j] == 0:
                for dj in range(N):
                    sum += map1[i][dj]
                for di in range(N):
                    sum += map1[di][j]
                sum = sum - map1[i][j]
                if sum > max_sum:
                    max_sum = sum
                if min_sum > sum:
                    min_sum = sum

    result = max_sum - min_sum
    print(f'#{tc} {result}')