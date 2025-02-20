#딱지놀이


N = int(input()) #라운드 수
for tc in range(1, N+1):
    A_list = [0] * 5 #A: 인덱스에 해당 카드 수 넣을 리스트
    B_list = [0] * 5 #B: 인덱스에 해당 카드 수 넣을 리스트
    A_N, *A_P = map(int,input().split()) #A 그림개수, 모양 리스트
    B_N, *B_P = map(int,input().split()) #B 그림개수, 모양 리스트
    result = 'C' #작동이 하는지 안하는지 보기 위해서 정답이 나올 수 없는 값으로 설정

    for A_pic in A_P: #A의 모양 리스트를 돌면서
        A_list[A_pic] += 1 #A_list 값 만들어주기
    
    for B_pic in B_P: #B의 모양 리스트를 돌면서
        B_list[B_pic] += 1 #B_list 값 만들어주기

    #별:4 원:3 사각형:2 삼각형:1
    #별의 개수가 다를 때
    if A_list[4] != B_list[4]:
        #별의 개수 큰 사람이 이김
        if A_list[4] > B_list[4]:
            result = 'A'
        else:
            result = 'B'
    
    #별의 개수가 같을 때
    else:
        #원의 개수가 다를 때
        if A_list[3] != B_list[3]:
            #원의 개수 큰 사람이 이김
            if A_list[3] > B_list[3]:
                result = 'A'
            else:
                result = 'B'
        #원의 개수가 같을 때
        else:
            #사각형의 개수가 다를 때
            if A_list[2] != B_list[2]:
                #사각형의 개수 큰 사람이 이김
                if A_list[2] > B_list[2]:
                    result = 'A'
                else:
                    result = 'B'
            #사각형의 개수가 같을 때
            else:
                #삼각형의 개수가 다를 때
                if A_list[1] != B_list[1]:
                    #삼각형의 개수 큰 사람이 이김
                    if A_list[1] > B_list[1]:
                        result = 'A'
                    else:
                        result = 'B'
                #삼각형의 개수가 같을 때
                #비김
                else:
                    result = 'D'
    
    print(result)