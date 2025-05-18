'''
BOJ14888 연산자 끼워넣기

# 입력
N : 숫자의 개수
numbers : N개의 숫자
ops : 연산자 개수 (+, -, *, // 순서)

# 구조
DFS를 통해 모든 연산자 순열을 탐색
중복 연산 제거를 위해 ops 배열을 감소/복구하며 백트래킹
연산 우선순위 없이 앞에서부터 순서대로 계산
음수 나눗셈은 문제 조건에 따라 따로 처리
최대값, 최소값을 갱신하면서 차이를 구함


'''

def dfs(cnt, total):
    global max_val, min_val
    if cnt == N - 1:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return

    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1

            if i == 0:
                dfs(cnt + 1, total + numbers[cnt + 1])
            elif i == 1:
                dfs(cnt + 1, total - numbers[cnt + 1])
            elif i == 2:
                dfs(cnt + 1, total * numbers[cnt + 1])
            elif i == 3:
                if total < 0:
                    dfs(cnt + 1, -(-total // numbers[cnt + 1]))
                else:
                    dfs(cnt + 1, total // numbers[cnt + 1])
            ops[i] += 1

N = int(input())
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_val = -float('inf')
min_val = float('inf')

dfs(0, numbers[0])
print(max_val)
print(min_val)