T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    numbers = [0] * (N+1)
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            numbers[j] = i
    result = " ".join(map(str, numbers[1:]))
    print(f'#{tc} {result}')