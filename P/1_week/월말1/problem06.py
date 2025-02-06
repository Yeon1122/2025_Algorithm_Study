############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
def find_max_position(matrix):
    # matrix의 크기를 n에 할당
    n = len(matrix)
    # 최대값과 그의 좌표를 찾기 위한 변수 생성, 0과 빈 리스트 할당
    max_value = 0
    max_position = []
    # maxtrix의 각 행을 순회하여 행의 최대값을 max_value와 비교,
    # 더 크다면 최대값을 새로 할당하고 max_position에 행 번호와 최대값의 index의 리스트를 할당
    for i in range(n):
        max_in_row = max(matrix[i])
        if max_in_row > max_value:
            max_value = max_in_row
            max_position = [i, matrix[i].index(max_in_row)]
    # 최대값의 좌표를 가리키는 리스트 반환
    return max_position    
    


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
