'''
N*N



3
5
19 57 74 73 94
26 27 32 98 61
40 88 49 38 25
21 66 53 95 46
80 23 58 39 89
7
40 49 56 83 84 31 11
42 95 12 16 21 19 26
98 93 29 68 10 92 82
23 13 24 58 35 25 47
17 66 39 67 70 14 87
22 34 46 94 69 96 89
62 88 50 51 61 71 86
9
90 57 65 18 25 93 64 11 54
95 19 80 37 63 44 15 14 10
89 59 46 70 38 36 21 51 97
53 47 60 88 40 48 79 56 55
83 13 27 86 45 71 75 28 84
30 20 29 35 99 98 61 94 23
85 42 43 22 16 77 31 78 34
74 26 73 92 50 72 87 49 32
68 24 91 12 17 82 69 67 81
'''
T= int(input())
for tc in range(1, T+1):
    N = int(input())
    ball_lst = [list(map(int, input().split())) for _ in range(N)]
    di = [0,-1,0,1]
    dj = [1,0,-1,0]
    mx = 0

    for i in range(N):
        for j in range(N):
            ci, cj = i, j
            cnt = 1
            while True:
                min_value = float('inf')
                for k in range(4):
                    ni = ci + di[k]
                    nj = cj + dj[k]

                    if 0 <= ni < N and 0 <= nj < N and ball_lst[ci][cj] > ball_lst[ni][nj]:
                        if min_value > ball_lst[ni][nj]:
                            min_value = ball_lst[ni][nj]
                            min_i = ni
                            min_j = nj
                            next_go = True

                if min_value == float('inf'):
                    mx = max(mx, cnt)
                    break

                ci = min_i
                cj = min_j
                cnt += 1


    print(f'#{tc} {mx}')



