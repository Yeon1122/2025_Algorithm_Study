############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def analyze_treasures(treasure_list, threshold):
    #보물 수 
    cnt = 1
    #threshold 수
    hold_cnt = 0
    #보물 딕셔너리
    treasures_dict = {}
    for i in range(0, len(treasure_list)):
        hold_cnt = 0
        #딕셔너리 추가
        if treasure_list != []:
            cnt = 1
            treasures_dict[treasure_list[i]] = cnt
        else:
            treasures_dict = {}
        #보물 수 세기
        for j in range(i):
            if treasure_list[i] == treasure_list[j]:
                cnt += 1
                treasures_dict[treasure_list[i]] = cnt
            else:   
                cnt = 1

    #threshold 세기
    #treasures_dict의 값을 추출
    treasure_value_list = list(treasures_dict.values())
    for i in treasure_value_list:

        if i > threshold:
            hold_cnt += 1

    return treasures_dict, hold_cnt
                
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 테스트 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(analyze_treasures(["gold", "silver", "gold", "diamond", "coin", "coin"], 1))
# ({'gold': 2, 'silver': 1, 'diamond': 1, 'coin': 2}, 2)

print(analyze_treasures([], 3))
# ({}, 0)

print(analyze_treasures(["pearl", "pearl", "ruby"], 2))
# ({'pearl': 2, 'ruby': 1}, 0)
#####################################################
