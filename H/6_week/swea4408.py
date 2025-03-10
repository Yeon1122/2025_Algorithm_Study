T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corridor = [0] * 201

    for _ in range(N):
        s, e = map(int, input().split())
        s, e = min(s, e), max(s, e)
        sn = (s + 1) // 2
        en = (e + 1) // 2

        for i in range(sn, en+1):
            corridor[i] += 1

    result = max(corridor)

    print(f"#{tc} {result}")