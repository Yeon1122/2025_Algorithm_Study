T=int(input())
for test_case in range(1, T+1):
    f_list = list(input().split())
    N = f_list.pop(0)
    # print(N)
    B, O = 1, 1
    b=[]
    o=[]
    for i in range(len(f_list)-1):
        if f_list[i] == 'B':
            b.append(int(f_list[i+1]))
        elif f_list[i] == 'O':
            o.append(int(f_list[i+1]))

    n = 0
    num = 0
    ans_cnt = 0
    ############
    #
    # 반복문 한 바퀴에 B와 O가 한 번씩 늘어나야함
    # B 또는 O가 스위치에 도착했을 때는 둘 중 스위치를 누르지 않는 애만 늘어나야함
    # 누르는 순서를 알아야함
    # #

    for i in range(0, len(f_list)-1,2):
        #만약 B를 먼저 눌러야하는 경우
        if f_list[i] == 'B':
            for j in range(b[num]):
                B += 1
                O += 1
                ans_cnt += 1
                #B가 목적지에 도착하기 전에 O가 도착한 경우
                if len(O) != 0:
                    if O == o[n]:
                        B += 1
                        ans_cnt += 1
                        if n < len(o):
                            n += 1
                        #O이 먼저 도착하고 B가 도착한 경우
                        if B == b[num]:
                            O += 1
                            ans_cnt += 1
                            if num < len(b):
                                num += 1
                    elif O!=o[n]:
                        continue
                else:
                    while B != b[num]:
                        B += 1
                        ans_cnt += 1

                    if num < len(b):
                        num += 1


        elif f_list[i] == 'O':
            for j in range(o[n]):
                B += 1
                O += 1
                ans_cnt += 1
                # B가 목적지에 도착하기 전에 B가 도착한 경우
                if len(b) != 0:
                    if B == b[num]:
                        B += 1
                        ans_cnt += 1
                        if num < len(b):
                            num += 1
                        # O이 먼저 도착하고 O가 도착한 경우
                        if O == o[n]:
                            O += 1
                            n += 1
                            ans_cnt += 1
                            if n < len(o):
                                n += 1
                    elif B!=b[num]:
                        continue
                else:
                    while O != o[n]:
                        O += 1
                        ans_cnt += 1

                    if num < len(o):
                        n += 1
    print(ans_cnt)

    # w = False
    # while w == False:
    #     if
    # # print(max_n)