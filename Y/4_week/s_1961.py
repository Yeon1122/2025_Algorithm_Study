##################
# 전역변수 T
# N:가로*세로
# nums = 2중 리스트
# 
# 1. 리스트회전
#   세로로 아래에서 위로 순회
#   ->열 중심으로 역으로 순회
#   출력을 위해서 회전한 값을 저장해줘야함
#   =>출력 ->2차원 배열의 첫 줄을 ' '를 구분자로 한 줄로 총 3줄 저장
#   => 회전 값 저장 -> 저장된 행을 행 중심으로 순회, 프린트
# #

T = int(input())
for test_case in range(1, T+1):
    
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    def rotate(li):
        new_nums = []
        #회전을 위한 반복문
        for j in range(0, N):
            new_nums.append([])
            for i in range(N-1, -1, -1):
                #이중리스트 형태로 저장
                # print(nums[i][j])
                new_nums[j].append(li[i][j])
        return new_nums
    
    result_90 = rotate(nums)
    result_180 = rotate(result_90)
    result_270 = rotate(result_180)

    #출력 양식
    print(f'#{test_case}')
    for i in range(N):
        print(''.join(map(str, result_90[i])), end = ' ')
        print(''.join(map(str, result_180[i])), end = ' ')
        print(''.join(map(str, result_270[i])), end = ' ')
        print()