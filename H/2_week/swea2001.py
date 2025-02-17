T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            total_sum = 0
            for x in range(M):
                for y in range(M):
                    total_sum += array[i + x][j + y]
            result = max(result, total_sum)
    
    print(f"#{t} {result}")