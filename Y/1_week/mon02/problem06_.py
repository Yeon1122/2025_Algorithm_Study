############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
def find_max_position(matrix):
    max = matrix[0][0]
    x=0
    y=0
    idx_li = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            #print(matrix[i][j])
            if max < matrix[i][j]:
                max = matrix[i][j]
                x = i
                y = j
            else:
                continue
    idx_li.append(x)
    idx_li.append(y)
    return idx_li

 
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

matrix3 = [
    [9, 2, 5],
    [4, 9, 6],
    [7, 8, 1]
]
#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_max_position(matrix1))  # [2, 2]
print(find_max_position(matrix2))  # [0, 0]
print(find_max_position(matrix3))  # [0, 0]
#####################################################