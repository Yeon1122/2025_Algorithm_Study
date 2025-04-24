T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    rocks = list(map(int,input().split()))
    for _ in range(M):
        i, j = map(int,input().split())
        for k in range(1,j+1):
            if 0 <= i-k-1 < N and 0 <= i+k-1 < N:
                if rocks[i-k-1] == rocks[i+k-1]:
                    rocks[i-k-1], rocks[i+k-1] = 1-rocks[i-k-1], 1-rocks[i+k-1]
 
    print(f"#{tc}",*rocks)
                              