def start_end(graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                start = [i, j]
            if graph[i][j] == 'Y':
                end = [i, j]
    return start, end

def go_RC(cur_pos, end_pos, command_str, graph, cur_dir_idx):
    cur_pos = start_point[:]
    visited = [[0] * N for _ in range(N)]
    for command in command_str:
        if command == 'L' or command == 'R':
            cur_dir_idx += commands[command]
            cur_dir_idx %= 4

        if command == 'A':
            if cur_dir_idx == 0:
                cur = (cur_pos[0] - commands['A'])
                if 0<=cur<N and 0<=cur_pos[1]<N and graph[cur][cur_pos[1]] != 'T':
                    cur_pos[0] = cur


            if cur_dir_idx == 1:
                cur = (cur_pos[1] + commands['A'])
                if 0 <= cur_pos[0] < N and 0 <= cur < N and graph[cur_pos[0]][cur] != 'T':
                    cur_pos[1] = cur


            if cur_dir_idx == 2:
                cur = (cur_pos[0] + commands['A'])
                if 0 <= cur < N and 0 <= cur_pos[1] < N and graph[cur][cur_pos[1]] != 'T':
                    cur_pos[0] = cur


            if cur_dir_idx == 3:
                cur = (cur_pos[1] - commands['A'])
                if 0 <= cur < N and 0 <= cur < N and graph[cur_pos[0]][cur] != 'T':
                    cur_pos[1] = cur
                    # visited[cur_pos[0]][cur_pos[1]] = 1

    # print(visited)
    if cur_pos == end_pos:
        return 1
    else:
        return 0






T = int(input())#테스트케이스
dr = [-1,0,1,0]
dc = [0,1,0,-1]
commands = {
    'A': 1,#앞으로 +1 또는 -1
    'L': -1,#
    'R': 1
}
for test_case in range(1, T+1):
    N = int(input())#필드 넓이
    map_list = [list(input()) for _ in range(N)] #지도
    start_point, end_point = start_end(map_list)#시작점 찾기
    # print(start_point, end_point)

    dir = [8,6,2,4] #시작은 cur_dir[0]
    cur_dir = 0%4

    ans_list = []
    command_list = []
    command_nums = []
    Q = int(input())
    for _ in range(Q):
        C, command = input().split()
        C = int(C)
        ans = go_RC(start_point,end_point, command, map_list, cur_dir)
        # print(ans)
        ans_list.append(ans)

    print(f'#{test_case}',*ans_list )

