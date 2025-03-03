# # 필요 데이터
# N : 주사위 개수
# dice_lists[N][6] : 주사위 상태 
# dices_copy[N][6] : 주사위 상태를 제거하기 위한 백업 데이터
# temp_sum : 임시 저장 총합
# max_sum : 전체 최대 총합

# # TC 진행
# 1. N, dice_lists 입력

# 2. 밑면 선정 > for 1~6

#   - 주사위 자료 백업 > 데이터 필요하겠다(깊은 복사)

#   temp_sum = 0
#   ㄱ. 각 주사위 제거 숫자 찾기 > for 0 ~ N-1
       
#        - 각 주사위 별 밑면 / 윗면 삭제
#        - 각 주사위 별 최대값 찾기 > temp_sum 누적

#   ㄴ. temp_sum과 max_sum 비교 후 갱신

from copy import deepcopy

# 주사위의 맞은편 면 (A-F, B-D, C-E)
opposite = [5, 3, 4, 1, 2, 0]

N = int(input())
dice_lists = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0

# 첫 번째 주사위 밑면을 모든 경우(0~5)에 대해 시도
for i in range(6):
    temp_sum = 0
    bottom_value = dice_lists[0][i]  # 첫 번째 주사위의 밑면 값 설정
    top_value = dice_lists[0][opposite[i]]  # 첫 번째 주사위의 윗면 값 설정

    # 첫 주사위의 옆면 중 최댓값을 더하기
    side_max = max([dice_lists[0][j] for j in range(6) if j not in [i, opposite[i]]])
    temp_sum += side_max

    # 두 번째 주사위부터 처리
    for j in range(1, N):
        bottom_idx = dice_lists[j].index(top_value)  # 현재 주사위의 밑면 idx
        top_idx = opposite[bottom_idx]  # 현재 주사위의 윗면 idx
        top_value = dice_lists[j][top_idx]  # 다음 주사위의 윗면 값 갱신

        # 현재 주사위에서 옆면 중 최댓값 찾기
        side_max = max([dice_lists[j][k] for k in range(6) if k not in [bottom_idx, top_idx]])
        temp_sum += side_max

    # 최대값 갱신
    max_sum = max(max_sum, temp_sum)

print(max_sum)