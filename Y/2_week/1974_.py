T= int(input())

for test_case in range(1, T+1):
    st_li = [list(map(int, input().split()))for _ in range(9)]
    result = -1
    visited = [0]*9
    st_i = 0
    st_j = 0
    st_9 = -1

    # print(st_li)
    # print(visited)

    

    for i in range(len(visited)):
        visited = [0]*9
        #print()
        st_i = 1
        for j in range(len(visited)):
            #print(st_li[i][j])
            visited[st_li[i][j]-1] += 1
            if visited[st_li[i][j]-1] >1:
                #print(-1)
                st_i = -1
                break
            else:
                st_i = 1
        if st_i == -1:
            break


    for j in range(len(visited)):
        visited = [0]*9
        #print()
        st_j = 1
        for i in range(len(visited)):
            #print(st_li[i][j])
            visited[st_li[i][j]-1] += 1
            #print(visited)
            if visited[st_li[i][j]-1] != 1:
                #print(-1)
                st_j = -1
                break
            else:
                st_j = 1
        if st_j == -1:
            break

    dr = [-1, -1, 0, 1, 1, 1, 0, -1, 0]
    dc = [0, 1, 1, 1, 0, -1, -1, -1, 0]
    for i in range(1, 8, 3):
        for j in range(1, 8, 3):
            visited = [0]*9
            #중심점 st_li[i][j]
            for d in range(0, 9):
                ni, nj = i+dr[d], j+dc[d]
                if 0<=ni<9 and 0<=nj<9:
                    #print(st_li[ni][nj])
                    visited[st_li[ni][nj]-1] += 1
                   # print(visited)
            if visited[st_li[i][j]-1] != 1:
                #print(-1)
                st_9 = -1
                break
            else:
                st_9 = 1
        if st_9 == -1:
            break
    if st_i == st_j == st_9 == 1:
        result = 1
        # print('1',1)
    else:
        result = 0
        # print('-1',-1)

    # print(st_i)
    # print(st_j)
    # print(st_9)
    print(f'#{test_case} {result}')