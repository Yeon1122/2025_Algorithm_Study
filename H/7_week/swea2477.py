import heapq
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    a_list = [0] + list(map(int, input().split())) # i번째 접수 창구 소요시간
    b_list = [0] + list(map(int, input().split())) # j번째 접수 창구 소요 시간
    t_list = [0] + list(map(int, input().split())) # 정비소 방문 시간

    welcome_desk = [0] * (N+1)
    repair_desk = [0] * (M+1)

    w_waitline = deque() # welcome 대기열
    r_waitline = deque() # repair 대기열

    time = []             # 시간 흐름
    for i in range(1, K+1): 
        time.append(t_list[i]) # 손님이 오는 시간대 체크

    max_num = 0
    mem_num = 1 

    temp_result = []
    
    while time:
        now = heapq.heappop(time)

        if mem_num <= K and t_list[mem_num] == now: # 손님 받을 시간이니 물어보기
            w_waitline.append(mem_num) # 접수대기열에 넣기
            mem_num += 1 # 다음 손님 기다리기

        for i in range(1, N+1):           # welcome_desk 비워주기
            # 현재시각 - 손님이 들어간 시간 == 창구별 소요시간
            if welcome_desk[i] != 0 and now - welcome_desk[i][0] == a_list[i]: 
                r_waitline.append(welcome_desk[i][1])
                welcome_desk[i] = 0       # welcome_desk 비워주기

        for i in range(1, M+1):           # repair_desk 비워주기
            if repair_desk[i] != 0 and now - repair_desk[i][0] == b_list[i]:
                repair_desk[i] = 0

        # 2-1.
        if w_waitline:                    # 대기열에서 welcome으로 넣기 (있을때 시도를 시작하고 싶어서서)
            for i in range(1, N+1):
                if welcome_desk[i] == 0 and w_waitline: #돌때마다 확인해야함 waitline 값 있는지
                    member = w_waitline.popleft()
                    welcome_desk[i] = (now, member)
                    heapq.heappush(time, now + a_list[i]) # 손님이 데스크 떠날때 시간 예상해서 time에 push
                    if i == A:
                        temp_result.append(member)

        if r_waitline:
            for i in range(1, M+1):
                if repair_desk[i] == 0 and r_waitline:
                    member = r_waitline.popleft()
                    repair_desk[i] = (now, member)
                    heapq.heappush(time, now + b_list[i])
                    if member in temp_result and i == B:
                        max_num += member
                        temp_result.remove(member) # 동일 손님이 여러번 오진 않으니 사실 필요없긴함

    if max_num == 0:
        max_num = -1

    print(f"#{tc} {max_num}")