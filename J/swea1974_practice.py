T = int(input())

for tc in range(1, T+1):
    
    range

    print(f'#{tc} {answer}')

# 가로줄 돌아가기
# ㄱ. 1부터 9까지 돌기 = range(9)
def is_valid_sudoku(grid):
    # 가로줄 검사
    for row in grid:
        if len(set(row)) != 9:
            return 0
        
#    > ㅑ번째 행에 대해서 중복 검사 > set 사용

# 세로줄 돌아가기
    # 세로줄 검사
    for c in range(9):
        col_nums = set()
        for r in range(9):
            col_nums.add(grid[r][c])
        if len(col_nums) != 9:
            return 0
# ㄱ. 1부터 9까지 돌기  = range(9)
#    > ㅑ번째 열에 대해서 중복 검사 > 앞이 자꾸 바뀜뀜

# 3*3 작은 격자 돌아가기 = range(9)
#    > ㅑ번째 3*3 박스에 대해서 중복 검사 > 파리퇴치 활용
    for start_r in range(0, 9, 3):
        for start_c in range(0, 9, 3):
            box_nums = set()
            for i in range(3):
                for j in range(3):
                    box_nums.add(grid[start_r + i][start_c + j])
            if len(box_nums) != 9:
                return 0
    
    return 1
