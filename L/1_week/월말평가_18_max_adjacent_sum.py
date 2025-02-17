############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
def max_adjacent_sum(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    N = len(matrix)
    new_matrix = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            new_matrix[i][j] = matrix[i][j]
            if j-1 >= 0:
                new_matrix[i][j] += matrix[i][j-1]
            
            if j+1 < N:
                new_matrix[i][j] += matrix[i][j+1]
            
            if i-1 >= 0:
                new_matrix[i][j] += matrix[i-1][j]

            if i+1 < N:
                new_matrix[i][j] += matrix[i+1][j]
    
    max_sum = new_matrix[0][0]

    for i in range(N):
        for j in range(N):
            if new_matrix[i][j] > max_sum:
                max_sum = new_matrix[i][j]

    return max_sum

    

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
