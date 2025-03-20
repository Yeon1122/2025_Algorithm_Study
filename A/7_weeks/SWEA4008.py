'''
SWEA4008

# 입력데이터
T : tc
tc
N : 숫자의 개수
op : list
graph[N][N]

# 구조
조합 or dfs인데 중복 연산 제거?
dfs(cnt,sum)
'''
T = int(input())

def dfs(cnt, sum):
    global max_sum, min_sum
    if cnt == N-1:
        max_sum = max(sum,max_sum)
        min_sum = min(sum,min_sum)
        return
    for k in range(4):
        if op[k] > 0:
            if k == 0:
                op[0] -= 1
                dfs(cnt + 1, sum + graph[cnt+1])
                op[0] += 1
            elif k == 1:
                op[1] -= 1
                dfs(cnt + 1, sum - graph[cnt+1])
                op[1] += 1
            elif k == 2:
                op[2] -= 1
                dfs(cnt + 1, sum * graph[cnt+1])
                op[2] += 1
            else:
                op[3] -= 1
                dfs(cnt + 1, int(sum / graph[cnt+1]))
                op[3] += 1
    return

for tc in range(1, T+1):
    N = int(input())
    op = list(map(int,input().split()))
    graph = list(map(int,input().split()))
    max_sum = float('-inf')
    min_sum = float('inf')

    dfs(0,graph[0])

    print(f'#{tc} {max_sum-min_sum}')
