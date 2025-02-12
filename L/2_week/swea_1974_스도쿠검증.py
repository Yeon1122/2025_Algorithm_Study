# 스도쿠 검증
# [입력]
T = int(input()) # T : 테스트 케이스의 개수

for test_case in range(1, T+1):
    puzzle = [list(map(int,input().split())) for _ in range(9)] # puzzle: 테스트 케이스(9*9) 퍼즐 데이터

    # [처리]
    # *변수
    result = 0 # result: 성공여부 (성공 1, 실패 0)

    # 가로줄이 모두 1-9 숫자가 겹치지 않는지
    def iCheck(p):
        for i in range(9):
            iCheck_puzzle = sorted(p[i])
            if iCheck_puzzle != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return 0
        return 1

    # 세로줄이 모두 1-9 숫자가 겹치지 않는지
    def jCheck(p):
        j_puzzle = [list(x) for x in zip(*p)]
        for j in range(9):
            j_puzzle[j].sort()
            if j_puzzle[j] != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return 0
        return 1

    # 3*3크기의 숫자가 겹치지 않는지
    def matrixCheck(p):
        di = [0, -1, 1, 0, -1, 1, 0, -1, 1]
        dj = [0, 0, 0, 1, 1, 1, -1, -1, -1]

        for i in range(0,9,3):
            for j in range(0,9,3):
                temp_list = []
                for di in range(3):
                    for dj in range(3):
                        temp_list.append(p[i + di][j + dj])
                temp_list.sort()
                if temp_list != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return 0
        return 1
    
    result = iCheck(puzzle) and jCheck(puzzle) and matrixCheck(puzzle)

    # [결과]
    print(f'#{test_case} {result}')
