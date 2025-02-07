############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 set, sum 등 사용 시 감점

def analyze_items(items_list):
    #중복 제거한 리스트
    value = []
    #양수, 음수 합계 변수수
    plu_sum = 0
    min_sum = 0

    #중복 제거
    for i in items_list:
        if i not in value : 
            value.append(i)
    
    #양수, 음수, 정수가 아닌 것을 골라내는 반복문문
    for i in value:
        if type(i)==int and i >=0:
            plu_sum += i
        elif type(i)==int and i <=0:
            min_sum += i
        else:
            continue

    return value, plu_sum, min_sum


    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(analyze_items([2, 2, 2, "a", "a", 3, 0, -2]))
# 예시 결과: ([2, "a", 3, 0, -2], (5, -2))

print(analyze_items([]))
# 예시 결과: ([], (0, 0))

print(analyze_items(["apple", "apple", "banana"]))
# 예시 결과: (["apple", "banana"], (0, 0))
#####################################################
