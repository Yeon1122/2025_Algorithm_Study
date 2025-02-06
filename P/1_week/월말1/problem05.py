############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def count_happy(diary):
    # happy 등장 횟수를 세기 위한 변수에 0 할당
    happy_count = 0
    # diary의 각 글자를 순회하여, 각 글자로 시작하는 5글자 단어가 happy라면 카운트 1 증가
    for i in range(len(diary)):
        if diary[i:i+5] == 'happy':
            happy_count += 1
    # happy 등장 횟수 카운트 반환
    return happy_count

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

a = '012345'
print(a[3:10])