#############
# 참외밭의 넓이 = 전체 넓이 - 작은 사각형
# 1 2 3 4 동 서(가로) 남 북(세로)
# 모양이 만들어지려면 세로 또는 가로에서 꺾어져야함.
# 가장 긴 변을 기준으로 양 옆을 빼주면 작은 부분의 길이가 나옴
# -> 짧은 부분은 작은 사각형의 가로세로 값을 보장하지 못 함(튀어나온 부분이 짧게 튀어나올 수 있음)
# -> 긴 변을 기준으로 거리를 구해주기#




K = int(input())
total_len = []
max_width = float('-inf')
max_height = float('-inf')
for i in range(6):
    d, l  = map(int, input().split())
    total_len.append(l)
    if d == 1 or d == 2:
        if max_width<l:
            max_width = l
    else:
        if max_height<l:
            max_height = l

box = max_height*max_width

# print(max_height, max_width, total_len)

max_width_idx = total_len.index(max_width)
max_height_idx = total_len.index(max_height)

sm_height = abs(total_len[(max_width_idx+1)%6]-total_len[(max_width_idx-1)%6])
sm_width = abs(total_len[(max_height_idx+1)%6]-total_len[(max_height_idx-1)%6])

# print(sm_width, sm_height)

sm_box = sm_height * sm_width
farm = box-sm_box
ans = K*farm

print(ans)