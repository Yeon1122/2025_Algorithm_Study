T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    costs = list(map(int, input().split()))
    max_cost = 0
    profit = 0
    for i in range(N - 1, -1, -1):
        if costs[i] > max_cost:
            max_cost = costs[i]
        else:
            profit += max_cost - costs[i]
    print(f"#{tc} {profit}")