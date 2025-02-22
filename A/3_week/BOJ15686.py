'''
치킨집의 좌표를 받아서 0처리를 하고 M개의 조합으로 치킨집을 둘 수 있는 경우의 수를 세고,
치킨 거리를 계산한다. 각 치킨 거리는 최솟값이어야 함.
그리고 모든 치킨 거리를 더하고, 그 중의 최솟값을 구한다.

5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5
'''
# N과 M
import itertools
from copy import deepcopy
N, M  = map(int,input().split())
town = [list(map(int,input().split())) for _ in range(N)]
house = []
chicken_store = []

def chicken(build_chicken, house):
    total = 0
    for x1,y1 in house: # x1,y1 : 집 좌표 주소
        short_cut = float('inf')
        for x2,y2 in build_chicken: # x2, y2 : 치킨 집 좌표 주소
            short_cut = min(short_cut, abs(x1-x2)+abs(y1-y2)) # 모든 치킨집 배치 후 거리 구하기
        total += short_cut
    return total

# 치킨 집 위치와 집 찾기
for i in range(N):
    for j in range(N):
        if town[i][j] == 2:
            chicken_store.append((i,j))
            # 들어가서 2를 0으로 바꿔줘야하나 0으로 다 바꾸고 그 위치에 2를 넣고 계산해야하나
        if town[i][j] == 1:
            house.append((i,j))

min_dis = float('inf')
for build_chicken in itertools.combinations(chicken_store,M):
    chicken_select_dis = chicken(build_chicken, house)
    min_dis = min(min_dis,chicken_select_dis)

print(min_dis)

