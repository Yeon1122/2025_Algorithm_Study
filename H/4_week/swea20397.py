T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1
        for c in range(1, j+1):
            if i-c >= 0 and i+c < len(stones):
                if stones[i-c] == stones[i+c]:
                    stones[i-c] = 1 - stones[i-c]
                    stones[i+c] = 1 - stones[i+c]
            else:
                break
    print(f"#{tc} " + " ".join(map(str, stones)))