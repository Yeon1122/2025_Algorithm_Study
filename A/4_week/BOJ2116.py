from copy import deepcopy
'''
        # copy_dice[j].pop(under)
        # if under == 0:
        #     up = copy_dice[j][5]
        #     under = copy_dice[j+1].index(up)
        # elif under == 1:
        #     up = copy_dice[j][3]
        #     under = copy_dice[j+1].index(up)
        # elif under == 2:
        #     up = copy_dice[j][4]
        #     under = copy_dice[j+1].index(up)
        # elif under == 3:
        #     up = copy_dice[j][1]
        #     under = copy_dice[j+1].index(up)
        # elif under == 4:
        #     up = copy_dice[j][2]
        #     under = copy_dice[j+1].index(up)
        # elif under == 5:
        #     up = copy_dice[j][0]
        #     under = copy_dice[j+1].index(up)
        # copy_dice[j].remove(up)
        # if j == N-1:
        #     copy_dice[j+1].pop(under)
        
# 필요 데이터
N : 주사위 개수
graph[N][6] : 주사위 상태 
graph_copy[N][6] : 주사위 상태를 제거하기 위한 백업 데이터
temp_sum : 임시 저장 총합
max_sum : 전체 최대 총합

# TC 진행
1. N, graph 입력

2. 밑면 선정 > for 1~6

  - 주사위 자료 백업 > 데이터 필요하겠다(깊은 복사)

  temp_sum = 0
  ㄱ. 각 주사위 제거 숫자 찾기 > for 0 ~ N-1
       
       - 각 주사위 별 밑면 / 윗면 삭제
        1) 인덱스를 찾아서 그에 맞는 인덱스 제거 후 다음 
       - 각 주사위 별 최대값 찾기 > temp_sum 누적

  ㄴ. temp_sum과 max_sum 비교 후 갱신
  

'''

N = int(input())
dice = [list(map(int,input().split())) for _ in range(N)]
mx = 0
info = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}


for i in range(1,7):
    copy_dice = deepcopy(dice)
    dice_sum = 0
    under = i
    for j in range(N):
      under_idx = copy_dice[j].index(under) # up의 인덱스
      up_idx = info[under_idx]
      up = copy_dice[j][up_idx]

      available_num = [copy_dice[j][k] for k in range(6) if k != under_idx and k != up_idx]
      dice_sum += max(available_num)
          
      under = up

    mx = max(dice_sum,mx)
print(mx)
