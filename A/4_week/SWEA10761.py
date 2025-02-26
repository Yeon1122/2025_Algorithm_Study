'''
입력:
T : tc 수
button : robot 버튼 (0:버튼의 수 , 1:: 버튼의 케이스)
blue = []
orange = []
button_order
blue_pos = 1
orange_pos = 1
cnt = 0

button.pop(0) 으로 버튼 수 받고
for str in button
    1) if문으로 Blue는 블루에 Orange는 오렌지에 (수만 받아야 편할듯)
     ㄱ) 각 색에 맞춰 리스트에 append
     ㄴ) button_order에 추가

while button_order: 버튼 팝을 이용

    button[0] idx 확인

    blue_pos(수만 받아야 할듯)와 blue[0]과 비교
    orange_pos와 orange[0]과 비교해서 이동

    버튼 도착하면,button_order과 맞으면 blue.pop & order.pop

'''

T = int(input())

for tc in range(1,T+1):
    button = list(input().split())
    blue = []
    orange = []
    button_order = []
    blue_pos = 1
    orange_pos = 1
    cnt = 0
    button_num = button.pop(0)

    for i in range(len(button)):
        if button[i] == 'B':
            blue.append(int(button[i+1]))
            button_order.append(button[i])
        if button[i] == 'O':
            orange.append(int(button[i + 1]))
            button_order.append(button[i])

    while button_order:
        if orange:
            if orange_pos == orange[0]:
                if button_order[0] == 'O':
                    orange.pop(0)
                    button_order.pop(0)
                
                    if not button_order:
                        cnt += 1
                        break

            elif orange_pos > orange[0]:
                orange_pos -= 1
            elif orange_pos < orange[0]:
                orange_pos += 1
            else: # 같은 경우
                pass

        if blue:
            if blue_pos == blue[0]:
                if button_order[0] == 'B':
                    blue.pop(0)
                    button_order.pop(0)
                    if not button_order:
                        cnt += 1
                        break

            elif blue_pos > blue[0]:
                blue_pos -= 1
            elif blue_pos < blue[0]:
                blue_pos += 1
            else:# 같은 경우
                pass


        # if blue:
        #     if blue_pos == blue[0]:
        #         if button_order[0] == 'B':
        #             blue.pop(0)
        #             button_order.pop(0)
        #             if not button_order:
        #                 cnt += 1
        #                 break
        #             cnt += 1
        #             continue
        # if orange:
        #     if orange_pos == orange[0]:
        #         if button_order[0] == 'O':
        #             orange.pop(0)
        #             button_order.pop(0)
        #             if not button_order:
        #                 cnt += 1
        #                 break
        #             cnt += 1
        #             continue

        cnt += 1

    print(f'#{tc} {cnt}')