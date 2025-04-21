T = int(input())    # 인풋값 받기

for tc in range(1, T+1):        #1부터 T+1까지 tc돌기
    
    N = int(input())            # N정수값 받기
    numbers = []                # numbers에 빈리스트 저장
    for i in range(N):          # N번 i가 돈다. 쪼개서 저장해서 빈리스트에 넣기.
        numbers.append(list(map(int, input().split())))

    turns = []                  # turns에 90, 180, 270도 넣을 행렬 저장

    for i in range(3):          # i세번 돈다
        temp_arr = []           # 90도 회전한 행렬 담을 빈리스트
        for i in range(N):      # N번 i가 돈다. 
            cur_row = []        # 행에 빈리스트
            for j in range(N):  # N번 돈다.
                cur_row.append(numbers[N-1-j][i])   #관계식 설정. N-1 뒤 인덱스에서 j만큼 뺀다, i번째
            temp_arr.append(cur_row) # temp_arr에 currow를 담는다.
        turns.append(temp_arr)      #turns에 temp_arr을 담는다.

        numbers = temp_arr    #numbers에 temp_arr을 저장해준다.

    print(f'#{tc}')

    for i in range(N):
        
        for j in range(3):
            print(''.join(map(str, turns[j][i])), end=" ")      # 각 요소에 접근해서 string으로 바꿔준다.
        print()
        ########################################################################3
