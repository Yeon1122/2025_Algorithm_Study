'''
3가지 경우를 만들면 되는데,
가로줄 인 경우
세로줄 인 경우
3*3행렬 인 경우

set 함수를 사용하지 않았을 때, 쓸 수 있는 방법
==> counting
그래서 행렬을 나누는 작업을 먼저하면 좋을듯

1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9

1
7 3 6 4 8 9 2 5 1
8 5 2 7 3 1 6 9 4
9 1 4 5 6 2 7 3 8
4 9 7 2 5 6 8 1 3
5 6 3 1 8 7 9 4 2
2 8 1 9 4 3 5 6 7
6 7 5 3 2 4 1 8 9
1 4 9 6 7 8 3 2 5
3 2 8 1 9 5 4 7 6

'''

T = int(input())

for tc in range(1, T+1):
    sdq = []
    counts = [0] * 10
    check_1 = check_2 = check_3 = 1
    for i in range(9):
        sdq_lst = list(map(int, input().split()))
        sdq.append(sdq_lst)

    # 가로줄 검증
    for i in range(9):
        counts = [0] * 10
        for j in range(9):
            counts[sdq[i][j]] += 1

        if counts[1:10] != [1] * 9:
            check_1 = 0
            break


    # 세로줄 검증
    for i in range(9):
        counts = [0] * 10
        for j in range(9):
            counts[sdq[j][i]] += 1

        if counts[1:10] != [1] * 9:
            check_2 = 0
            break


    # 3*3 배열 검증
    lst_33 = []     # 3*3 배열을 넣을 리스트 생성
    for i in range(0,9,3):
        for j in range(0,9,3):
            lst = []
            for x in range(3):
                for y in range(3):
                    lst.append(sdq[i+x][j+y])
            lst_33.append(lst)

    for i in range(9):
        counts = [0] * 10
        for j in range(9):
            counts[lst_33[i][j]] += 1

        if counts[1:10] != [1] * 9:
            check_3 = 0
            break


    if check_1 and check_2 and check_3 :
        ans = 1
    else :
        ans = 0
    print(f'#{tc} {ans}')


