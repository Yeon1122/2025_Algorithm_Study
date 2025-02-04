############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 파이썬 내장 함수 min 함수를 사용하지 않습니다.
def min_score(scores):

    # inscore을 활용한 작은 수 구하기기
    # min_num = scores[0]

    # for i in scores:
    #     if i < min_num:
    #         min_num = i
    #     else:
    #         continue
    # return min_num

    #for in range(len)을 활용한 작은 수 구하기
    min_num = scores[0]
    for i in range(len(scores)):
        if min_num>scores[i-1]:
            min_num = scores[i-1]
        else:
            continue
    return min_num
    
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(min_score([30, 60, 90, 70])) # 30
print(min_score([0, 10, 20, 30, 40, 50])) # 0
print(min_score([50, 70, 50, 45, 80, 80])) # 45
#####################################################

# 테스트 코드는 이곳에
print(min_score([100, 100]))  