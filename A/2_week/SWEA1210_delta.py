'''
델타 탐색을 이용하고, 역추적 방식을 통해서 해봐야겠다.
처음에 주어진 사다리에서 마지막에 주어진 2의 인덱스를 찾아야겠다.

중요한 것은 델타 탐색의 방향의 우선 순위가 중요한 것 같다.
아래로 내려가는 델타는 필요 없고,
좌 우 상 탐색 / 상 좌 우로 나눠서 탐색을 해야하나?
'''

for tc in range(1, 11):
    T = int(input())
    ladder = []
    r = 99
    dr = [-1,0,0]
    dc = [0,-1,1] # 상 : 0, 좌 : 1, 우 : 2
    search_dir = [[1,2,0],[1,0],[2,0]]  # 와
    dir = 0

    for i in range(100):
        ladder_lst = list(map(int, input().split()))
        ladder.append(ladder_lst)

    c = ladder[99].index(2)

    while r > 0:
        for i in range(len(search_dir)):
            next_dir = search_dir[dir][i]
            nr = r + dr[next_dir]
            nc = c + dc[next_dir]

            if 0<=nr and 0<=nc<100 and ladder[nr][nc] == 1:
                dir = next_dir
                r = nr
                c = nc
                break
    print(f'#{tc} {c}')