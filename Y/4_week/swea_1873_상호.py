T = int(input())
for test_case in range(1, T+1):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    command_num = int(input())
    command_list = list(input())
    # print(H, W, field, command_num, command_list)

    #현재 내 위치 찾기
    for i in range(H):
        for j in range(W):
            if field[i][j] in '<>^v':
                cur_i = i
                cur_j = j
    # print(cur_i, cur_j)

    #조작하기
    # 위치 조작인지, 포탄 발사인지
    #1. 가고자 하는 위치 평지 여부
    #   1-1.평지인 경우
    #       1. 현재 위치 .
    #       2. 위치 값 갱신, 갱신 값 '<>^v'
    #   1-2 평지가 아닌 경우
    #       1. 전차 방향 전환
    # 현재 위치, 포탄 범위
    # 0<=cur_i, cur_j, si, sj <H W

    for i in range(command_num):

        # 포탄 발사인경우
        if command_list[i] =='S':
            #현재 위치에 포탄 위치 설정
            si, sj = cur_i, cur_j
            #강철 벽이 아니면 포탄이 맵 끝까지 직진
            while 0 <= si < H and 0 <= sj < W and field[si][sj] != '#':
                if field[cur_i][cur_j] == '^':
                    si -= 1
                elif field[cur_i][cur_j] == 'v':
                    si += 1
                elif field[cur_i][cur_j] == '<':
                    sj -= 1
                elif field[cur_i][cur_j] == '>':
                    sj += 1
                #벽돌 벽을 만나는 경우 벽돌 벽 하나를 없애고 평지로 만들기.
                if 0 <= si < H and 0 <= sj < W and field[si][sj] == '*':
                    field[si][sj] = '.'
                    break

        else:
            # 이동인경우
            if command_list[i] == 'U':
                if 0 <= cur_i-1 < H and 0 <= cur_j < W:
                    # 평지인 경우
                    if field[cur_i-1][cur_j] == '.':
                        field[cur_i][cur_j] = '.'
                        cur_i -= 1
                        field[cur_i][cur_j] = '^'
                    else:
                        field[cur_i][cur_j] = '^'
                else:
                    field[cur_i][cur_j] = '^'

            if command_list[i] == 'D':
                if 0 <= cur_i+1 < H and 0 <= cur_j < W:
                    # 평지인 경우
                    if field[cur_i+1][cur_j] == '.':
                        field[cur_i][cur_j] = '.'
                        cur_i += 1
                        field[cur_i][cur_j] = 'v'
                    else:
                        field[cur_i][cur_j] = 'v'
                else:
                    field[cur_i][cur_j] = 'v'

            if command_list[i] == 'L':
                if 0 <= cur_i < H and 0 <= cur_j-1 < W:
                    # 평지인 경우
                    if field[cur_i][cur_j-1] == '.':
                        field[cur_i][cur_j] = '.'
                        cur_j -= 1
                        field[cur_i][cur_j] = '<'
                    else:
                        field[cur_i][cur_j] = '<'
                else:
                    field[cur_i][cur_j] = '<'

            if command_list[i] == 'R':
                if 0 <= cur_i < H and 0 <= cur_j+1 < W:
                    # 평지인 경우
                    if field[cur_i][cur_j+1] == '.':
                        field[cur_i][cur_j] = '.'
                        cur_j += 1
                        field[cur_i][cur_j] = '>'
                    else:
                        field[cur_i][cur_j] = '>'
                else:
                    field[cur_i][cur_j] = '>'
            # print(field)
    result = '\n'.join(''.join(row) for row in field)

    print(f'#{test_case} {result}')
