T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stones = [0] + list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        for j in range(1, j+1):
            if 1 <= i-j <= N and 1 <= i+j <= N:
                if stones[i-j] == stones[i+j]:
                    stones[i-j] = 1- stones[i-j]
                    stones[i+j] = 1- stones[i+j]
    result = " ".join(map(str, stones[1:]))
    print(f'#{tc} {result}')