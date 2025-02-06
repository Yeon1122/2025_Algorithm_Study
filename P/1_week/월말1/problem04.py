############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 set, sum 등 사용 시 감점

def analyze_items(items_list):
    # 중복 제거 리스트를 만들기 위한 빈 리스트 생성
    final_list = []
    # 리스트가 비어있지 않다면 리스트를 순회하여 각 아이템이 이미 중복 제거 리스트에 있는지 확인,
    # 있다면 다음으로 넘어가고 없다면 중복 제거 리스트에 추가
    if items_list:
        for item in items_list:
            if item in final_list:
                continue
            else:
                final_list.append(item)        
    # 리스트가 비어 있다면 pass하여 기존의 빈 리스트로 유지
    else:
        pass
    
    # 양수와 음수의 합을 구하기 위한 변수에 0 할당
    pos_sum = 0
    neg_sum = 0
    # 중복 제거 리스트의 아이템을 순회하여 정수인지 확인
    for item in final_list: 
        # 정수라면 양수인지 음수인지 확인 후 해당하는 변수에 합함
        if isinstance(item, int):
            if item > 0:
                pos_sum += item
            if item < 0:
                neg_sum += item
            # 0이면 넘어가기
            else:
                continue
        # 정수가 아니라면 넘어가기
        else:
            continue
    # 중복을 제거한 리스트와 양수합과 음수합의 튜플 반환
    return final_list, (pos_sum, neg_sum)

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
