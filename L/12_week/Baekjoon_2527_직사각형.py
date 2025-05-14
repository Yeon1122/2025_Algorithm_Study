# for _ in range(4):
#     square = list(map(int, input().split()))
        
#     if square[0] < square[4]:
#         square_1 = square[0:4]
#         square_2 = square[4:8]
#     elif square[0] == square[4] and square[2] > square[6]:
#         square_1 = square[0:4]
#         square_2 = square[4:8]
#     else:
#         square_2 = square[0:4]
#         square_1 = square[4:8]

#     answer = 'z'

#     if square_1[2] < square_2[0]:
#         answer = 'd'
#     elif square_1[2] == square_2[0] and square_1[1] == square_2[3]:
#         answer = 'c'
#     elif square_1[2] == square_2[0] or square_1[1] == square_2[3]:
#         answer = 'b'
#     else:
#         answer = 'a'

#     print(answer)



for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 겹치지 않는 경우 (완전 분리)
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print('d')
    # 점으로 만나는 경우 (코너)
    elif (p1 == x2 or p2 == x1) and (q1 == y2 or q2 == y1):
        print('c')
    # 선분으로 만나는 경우 (한 줄이 겹침)
    elif p1 == x2 or p2 == x1 or q1 == y2 or q2 == y1:
        print('b')
    # 직사각형 겹침
    else:
        print('a')