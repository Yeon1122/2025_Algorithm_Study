def farm_profit(tc):
    results = []
    for t in range(tc):
        N = int(input().strip())                # 가로 세로 N인 농장의 크기
        farm = [list(map(int, list(input().strip()))) for _ in range(N)]   
        center = N // 2                         # 중앙값
        total_profit = 0
        for i in range(N):
            start = abs(center - i)             # 파란색 시작
            end = N - abs(center - i)           # 파란색 끝
            total_profit += sum(farm[i][start:end])
        results.append(f"#{t+1} {total_profit}")
    return results
tc = int(input().strip())
for result in farm_profit(tc):
    print(result)