# 필요 데이터
# 전역 : T, info, dr, dc
# TC 당 데이터 
# : H, W, graph, N, orders
#   r, c, nr, nc, dir

# 상하좌우 > 0123

# 로직

# 1. 탱크 위치 / 방향 파악
#    ^ : 0, v : 1, < : 2 , > : 3

# 2. orders 명령을 하나씩 수행
#    > for N
#    ㄱ. 포탄을 쏘는 것
#       a. 다음 지점 초기화
#       b. 쏠 수 있을 때까지 진행하기
#          - graph 범위 이내
#          - # 이나 *을 만나지 않았을 때   >  그게 아니라면 break
#          - 계속 진행할 수 있다면 다음 지점을 변경해주기

#    ㄴ. 이동 명령
#      a. 해당 명령의 방향을 파악하기
#         > U : 0, D : 1, L : 2, R : 3
#      b. 방향을 옮겨주기
#         > 0 : ^ , 1 : v , 2 : < , 3 : > 
#      c. 해당 방향으로 이동이 가능하다면 이동하기
#         > 0 : ^ , 1 : v , 2 : < , 3 : > 
T = int(input())
info = {'^': 0, 'v': 1, '<': 2, '>': 3, 'U': 0, 'D': 1, 'L': 2, 'R': 3, 0: '^', 1: 'v', 2: '<', 3: '>'}
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    H, W = map(int, input().split())
    graph = [list(input()) for _ in range(H)]
    N = int(input())
    orders = input()
    r = c = dir = -1
    
    for i in range(H):
        for j in range(W):
            if info.get(graph[i][j]) != None:
                r = i
                c = j
                dir = info.get(graph[i][j])
                break
        if r != -1:
            break

    for order in orders:
        if order == 'S':
            nr = r+dr[dir]
            nc = c+dc[dir]
            while 0 <= nr < H and 0 <= nc < W:
                if graph[nr][nc] == '#':
                    break
                elif graph[nr][nc] == '*':
                    graph[nr][nc] = '.'
                    break
                nr += dr[dir]
                nc += dc[dir]

        else:
            dir = info.get(order)
            graph[r][c] = info.get(dir)
            nr = r + dr[dir]
            nc = c + dc[dir]
            
            if nr < 0 or nr >= H or nc < 0 or nc >= W or graph[nr][nc] != '.':
                continue

            graph[r][c] = '.'
            graph[nr][nc] = info.get(dir)
            r = nr
            c = nc
    
    print(f'#{tc}', end=" ")
    for i in range(H):
        print(''.join(graph[i]))