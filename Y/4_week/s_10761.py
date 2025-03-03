#################################
# 전역 변수 T
# N total_list
# total_list의 [0]-> N으로 빼주기
# button_bo = list, B,O로 이루어진 버튼 누르는 순서
# b_button = list, B가 눌러야하는 버튼 수
# o_button = list, O가 눌러야하는 버튼 수 
# 총 이동한 횟수 cnt#
# 
# 1. total리스트에서 N값 구하기
# 2. 버튼을 누르는 순서와 각자 눌러야하는 버튼의 위치 찾아주기
#   total_list에서 O의 버튼과 B의 버튼 분리해주고 O와 B의 순서 남겨두기
# 3. 버튼 누르기
#   버튼을 누르기 위해서 얼마나 돌아야하는지 모름 -> while로 반복
#   B와 O가 각각 눌러야하는 위치를 찾아야함#
#   한 번 반복에 한 칸씩 이동
#   한 번 반복하면 cnt도 올라가야함
#   #
#   ->B,O에 1씩 추가
#       => #
    # a. 버튼 누르는 순서를 알아야함
    #     button_bo 순회하면서 첫 번째로 버튼을 누를 로봇 찾기
#         첫 번째로 버튼 누를 로봇이 도착할 때까지 돌기
#         만약 첫 로봇이 도착한 것 보다 다른 로봇이 빠른 경우 다른 로봇은 자기 숫자에서 더이상 늘어나지 않게 함.
#         만약 첫 로봇이 도착하면 flag = 1
#         순서가 끝나면 flag는 다시 0으로 바꾸기
#         다음 로봇이 자기 자리에 있으면 다시 flag= 1 
#         이걸 버튼 수만큼 반복#

T=int(input())
for test_case in range(1, T+1):
    total_list = list(input().split())
    N = int(total_list.pop(0))
    # print(N)
    B, O = 1, 1
    button_bo = []
    b_button=[]
    o_button=[]
    flag = 0
    cnt = 0
    for i in range(len(total_list)-1):
        if total_list[i] == 'B':
            button_bo.append(total_list[i])
            b_button.append(int(total_list[i+1]))
        elif total_list[i] == 'O':
            button_bo.append(total_list[i])
            o_button.append(int(total_list[i+1]))
    # print(button_bo, b_button, o_button)

    for i in range(N):
        flag = 0
    #순서가 B인 경우
        # print(button_bo[i])
        if button_bo[i] == 'B':
            
            while flag == 0:

                if B == b_button[0]:
                    if len(o_button)>0:
                        if o_button[0]>O:
                            O += 1
                        elif o_button[0]<O:
                            O -= 1
                    cnt += 1
                    flag = 1
                    b_button.pop(0)
                    
                elif b_button[0]>B:
                    if len(o_button)>0:
                        if o_button[0]>O:
                            O += 1
                        elif o_button[0]<O:
                            O -= 1
                    B += 1
                    cnt += 1
                else:
                    if len(o_button)>0:
                        if o_button[0]>O:
                            O += 1
                        elif o_button[0]<O:
                            O -= 1
                    B -=1
                    cnt += 1
                # print(O, B, 'cnt o', cnt)

#           순서가 O인 경우
        elif button_bo[i] == 'O':
            while flag == 0:
                if O == o_button[0]:
                    if len(b_button)>0:
                        if b_button[0]>B:
                            B += 1
                        elif b_button[0]<B:
                            B -=1
                    cnt += 1
                    flag = 1
                    o_button.pop(0)

                elif o_button[0]>O:
                    if len(b_button)>0:
                        if b_button[0]>B:
                            B += 1
                        elif b_button[0]<B:
                            B -=1
                    O += 1
                    cnt += 1
                else:
                    if len(b_button)>0:
                        if b_button[0]>B:
                            B += 1
                        elif b_button[0]<B:
                            B -=1
                    O -= 1
                    cnt += 1

                

                # print(O, B, 'cnt o', cnt)

    print(f'#{test_case} {cnt}')

            
