############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
def max_adjacent_sum(matrix):
    #max값 변수
    max_num = 0
    #행
    for i in range(len(matrix)):
        #열
        for j in range(len(matrix)):
            #합계 저장 변수
            num_sum = 0
            #델타 탐색 이용, 자기 자신도 포함하기!!
            for di, dj in [[0,1], [1,0], [-1,0], [0,-1],[0,0]]:
                #index 범위 설정해주기(list index out of range)
                if 0<=i+di<len(matrix) and 0<=j+dj<len(matrix):
                    num_sum += matrix[i+di][j+dj]

            if max_num < num_sum:
                max_num = num_sum
                
            else:
                continue
                

    print(max_num)
            
    # 여기에 코드를 작성하여 함수를 완성합니다.


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
#print(max_adjacent_sum(matrix2))  # 25
#####################################################
