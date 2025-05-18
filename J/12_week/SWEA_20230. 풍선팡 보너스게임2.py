'''

3
4
1 1 1 1
1 2 1 1
1 1 1 1
1 1 1 1
5
3 3 2 2 3
2 4 5 2 3
4 2 1 2 4
1 3 5 3 3
1 4 5 2 3
5
1 3 5 2 3
2 2 5 5 5
3 4 2 1 1
1 5 2 5 4
5 2 3 4 1

어떻게?
1. 시작점 찍기
2. 해당 행을 누적합
3. 누적합 상태에서 해당 열 누적합
4. 행을 밑으로 이동, 해당 행 누적합
5. 누적합 상태에서 해당열 모두 더하고 장

'''
# 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    balloons= [list(map(int, input().split())) for _ in range(N)]
    
    def pang(r, c, balloons):
        row_sum = sum(balloons[r])
        col_sum = sum(balloons[i][c] for i in range(N))
        score = row_sum + col_sum - balloons[r][c]

        return score
     
    scores = []
    for r in range(N):
        for c in range(N):
            scores.append(pang(r, c, balloons))
    
    ans = max(scores)
    print(f'#{tc} {ans}')

