############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def under_60(scores):
    count_values = 0
    for score in scores:
        if score < 60:
            count_values += 1
    return count_values

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(under_60([30, 60, 90, 70])) # 1
print(under_60([0, 10, 20, 30, 40, 50])) # 6
print(under_60([50, 70, 50, 45, 80, 80])) # 3
#####################################################
# 전체 점수 중 60점 미만인 과목의 개수 계산해 반환하는 under_60 함수 완성하기