'''
10 * 10 이 차원 행렬에서
괴물과 벽이 주어지고,
0 : 안전 구역 , 1 : R괴물(1칸) , 2 : G괴물(2칸), 3 : B괴물(3칸) , 4 : 벽
레이저 구역을 5로 설정해두고, 각 괴물별로 레이저를 발사 시킨다.
2중 for 문을 돌면서 델타로 탐색하고,
그 후 0의 개수를 찾으면 끝

'''
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    place = []
    sum = 0
    # 우 하 좌 상
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    for _ in range(10):
        place.append(list(map(int,input())))


    for i in range(10):
        for j in range(10):
            # 4와 5는 볼 필요 없음
            if place[i][j] == 4:
                continue
            if place[i][j] == 5:
                continue
            if place[i][j] >= 1: # ij의 개수만큼 +하면될듯
                for n in range(4): # 4방향 탐색
                    for k in range(1, place[i][j] + 1): # 괴물의 색에 따른 탐지 범위 2중 for문
                        ni = i + di[n] * k      #delta 탐색
                        nj = j + dj[n] * k
                        if 0 <= ni < 10 and 0 <= nj < 10:       # 배열의 크기만큼 인덱스 벗어나지 않게
                            if place[ni][nj] == 1:      # 가다가 괴물 or 벽을 만나면 break
                                break
                            if place[ni][nj] == 2:
                                break
                            if place[ni][nj] == 3:
                                break
                            if place[ni][nj] == 4:
                                break
                            place[ni][nj] = 5           # 그게 아니라면 5

                    # 1,2,3,4 중에 하나가 탐색이 되면, 그 방향의 탐색을 종료해야 함. break 쓰니까 되네

    for i in range(10): # 안전구역 0의 갯수 세기기
        sum += place[i].count(0)

    print(f'#{tc} {sum}')
