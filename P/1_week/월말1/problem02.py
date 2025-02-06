############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def analyze_treasures(treasure_list, threshold):
    # 딕셔너리 생성을 위해 value 기본값(0)을 담은 리스트 생성
    treasure_count = [0]*len(treasure_list)
    # 딕셔너리 생성 (중복 자동 제거)
    treasure_dict = dict(tuple(zip(treasure_list, treasure_count)))
    # treasure_list를 순회하여 보물이 나올 때마다 딕셔너리의 해당 보물 key값의 value를 1 증가
    for treasure in treasure_list:
        treasure_dict.update({treasure: treasure_dict.get(treasure)+1})
    
    # 임계값 초과 보물 수를 세기 위한 변수에 0 할당
    count_threshold = 0
    # treasure_dict를 순회하여 value 값이 임계값을 초과할 때마다 카운트 1 증가
    for i in treasure_dict.values():
        if i > threshold:
            count_threshold += 1
    # 딕셔너리와 임계값 초과 카운트 반환
    return treasure_dict, count_threshold

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
