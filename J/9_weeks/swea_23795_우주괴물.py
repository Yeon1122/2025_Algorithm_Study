# 델타배열(방향배열)
# 1. break랑 continue 잘써야한다.
# 2. while break를 활용 할 수 있어야한다.

# while 0 <= ny < N and 0 <= nx < N:
# 어느 조건문에 break? ---> 벽을 만났을떄 break

#0. 델타 세팅
dr = [-1, 1, 0, 0] # 상 하 좌 우
dc = [0, 0, -1, 1]

def monster(r, c):
    for dir in range(4):
        nr = r+dr[dir]
        nc = c+dc[dir]
        while 0<= nr < N and 0<= nc < N:
            if monstermap[nr][nc] == 0:
                monstermap[nr][nc] = 3
        # 벽만나면 브레이크
            elif monstermap[nr][nc] == 1:
                break
            nr += dr[dir]
            nc += dc[dir]

    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    monstermap = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    #괴물 위치 찾기
    for i in range(N):
        for j in range(N):
            if monstermap[i][j] == 2:
                r, c = i , j
                break
    monster(r, c)

#counting
    for i in range(N):
        for j in range(N):
            if monstermap[i][j] == 0:
                cnt += 1

    # print(monstermap)

    print(f'#{tc} {cnt}')