#라운드
T= int(input())
for round in range(1, T+1):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a_card_cnt = A.pop(0)# == len(A)
    b_card_cnt = B.pop(0)# == len(B)
    A.sort(reverse=True)
    B.sort(reverse=True)

    #쿠션 깔아주는 용도의 range 찾아주기
    min_card = min(a_card_cnt, b_card_cnt)
    max_card = max(a_card_cnt, b_card_cnt)
    cu = max_card-min_card

    #리스트 인덱스용 쿠션 깔아주기
    if cu>0:
        for i in range(cu):
            if len(A) < len(B):
                A.append(0)
            else:
                B.append(0)

    # print(A, B, a_card_cnt, b_card_cnt)

    #정렬 후 값 비교
    for i in range(len(A)):
        if A[i] > B[i]:
            result = 'A'
            # print('A')
            break
        elif B[i] > A[i]:
            result = 'B'
            # print('B')
            break
        else:
            result = 'D'
    

    print(result)

