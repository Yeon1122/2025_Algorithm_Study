N = 5 #자리 가로세로
K = 7 #7공주
seat = [list(input()) for _ in range(N)]
#delta
dr = [-1,0,1,0]
dc = [0,1,0,-1]
prin_7 = []
princess = [] #경우의 수들, ans = len(princess)
# print(seat)

def dfs(cur_r, cur_c):
    global prin_7, princess
    visited[cur_r][cur_c] = 1
    prin_7.append(seat[cur_r][cur_c])
    prin_cnt = prin_7.count('S')
    print(prin_7, prin_cnt,cur_r,cur_c, len(prin_7))

    # if len(prin_7)>=4:
    #     if prin_cnt < len(prin_7)-3:
    #         print('cnt-3', prin_7, prin_cnt)
    #         # prin_7.pop()
    #         # visited[cur_r][cur_c] = 0
    #         print(prin_7, 'pop')
    #         return
    #
    #     if len(prin_7) == 7:
    #         if prin_cnt >= 4:
    #             print('cnt7', prin_7)
    #             princess.append(prin_7)
    #             print('princess', princess)
    #             return princess

    if len(prin_7) == 7:
        if prin_cnt >=4:
            princess_7 = prin_7[:]
            princess.append(princess_7)
            # print(princess, 'princess')

        visited[cur_r][cur_c] = 0
        prin_7.pop()
        return



    for d in range(len(dr)):
        nr = cur_r + dr[d]
        nc = cur_c + dc[d]
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
            dfs(nr, nc)
            # print(prin_7, 'if pop', visited)

    visited[cur_r][cur_c] = 0
    prin_7.pop()


            # if len(prin_7)>=1:
            #     prin_7.pop()
            #     # visited[cur_r][cur_c] = 0

    # visited[cur_r][cur_c] = 0



visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if seat[i][j]  == 'S':
            visited = [[0] * N for _ in range(N)]
            prin_7 = []
            dfs(i,j)
            print()

print(princess)