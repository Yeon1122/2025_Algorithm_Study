T = 10

for test in range(1, T+1):
    test_case = int(input())
    #변수 설정
    #ladder = []
    start_i = 99
    start_j = 0
    answer = 0

    # #ladder리스트 내에 2차원 리스트 만들기
    # for i in range(100):
    #     ladder.append(list(map(int, input().split())))
    #리스트 컴프리헨션으로 변경
    ladder = [list(map(int, input().split())) for i in range(100)]

    #print(ladder)

    #시작점(사다리의 골)의 위치 찾기
    for j in range(len(ladder[99])):
        if ladder[99][j] == 2:
            start_j = j
            break
    #print(start_i, start_j)

    #시작점 주변 값 보기기
    while start_i>0:
        if start_j < 99 and ladder[start_i][start_j + 1] == 1:
            while start_j < 99 and ladder[start_i][start_j+1] == 1:
                start_j += 1
        elif start_j > 0 and ladder[start_i][start_j - 1] == 1:
            while start_j > 0 and ladder[start_i][start_j-1] == 1:
                start_j -= 1
        
            start_i -= 1

    
    print(f'#{test_case} {start_j}')