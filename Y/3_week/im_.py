T=int(input())
for test_case in range(1, T+1):
    N = int(input())
    ball_list = [list(map(int, input().split())) for _ in range(N)]
    #상 시계방향
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    cnts = []
    max_cnt = 0
    li_len = len(di)


    def search(i1, j1, li):
        next_vals = []
        global cnt
        dx = []
        dy = []
        for k in range(li_len):
            ni = i1 + di[k]
            nj = j1 + dj[k]

            if 0 <= ni < N and 0 <= nj < N and li[i1][j1] > li[ni][nj]:
                next_vals.append(li[ni][nj])
                dx.append(ni)
                dy.append(nj)

        if next_vals != []:
            next_val = min(next_vals)
            for i in range(len(next_vals)):
                if next_val == li[dx[i]][dy[i]]:
                    ni, nj = dx[i], dy[i]
                    search(ni, nj, li)
                    cnt+=1
                    
        return cnt


    for i in range(N):
        for j in range(N):
            cnt = 1
            ball = search(i, j, ball_list)
            cnts.append(cnt)
            answer = max(cnts)

    print(f'#{test_case} {answer}')