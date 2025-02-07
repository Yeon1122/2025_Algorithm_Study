############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def count_happy(diary):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    count = 0

    # diary 문장 처음부터 5글자까지 처음부터 문장 끝까지 하나씩 이동하면서 happy 찾기
    # happy가 있으면 count에 1 추가하기
    for i in range(len(diary)-4):
        if diary[i:i+5] == 'happy':
            count += 1

    return count

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(count_happy("I feel happy. HAPPY! so happy!"))  # 2
print(count_happy("happyhappy"))                      # 2
print(count_happy("nothing here"))                    # 0
#####################################################

