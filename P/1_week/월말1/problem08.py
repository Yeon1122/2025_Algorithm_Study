############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
def max_adjacent_sum(matrix):
    # matrix 크기를 n에 할당 
    n = len(matrix)
    # 최대값을 구하기 위한 변수에 0을 할당
    max_adj_sum = 0
    # 각 칸마다 주변 칸과의 합을 계산
    for i in range(n):
        for j in range(n):
            adj_sum = matrix[i][j]
            # 행렬의 범위를 벗어나지 않는 주변 영역만 합산
            if i != 0:
                adj_sum += matrix[i-1][j]
            if i != n-1:
                adj_sum += matrix[i+1][j]
            if j != 0:
                adj_sum += matrix[i][j-1]
            if j != n-1:
                adj_sum += matrix[i][j+1]
            # 그 칸의 주변 칸과의 합이 현재 max_adj_sum보다 크다면 그 값을 새로 할당
            if adj_sum > max_adj_sum:
                max_adj_sum = adj_sum
    # 주변 칸과의 합의 최대값 반환
    return max_adj_sum


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(max_adjacent_sum(matrix1))  # 29
print(max_adjacent_sum(matrix2))  # 25
#####################################################
