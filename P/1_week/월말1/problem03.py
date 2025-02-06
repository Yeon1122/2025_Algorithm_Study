############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def find_most_populated(animal_map):
    if animal_map:
        # 가장 개체 수가 많은 동물과 그 수를 찾기 위한 변수 생성, 빈 스트링과 0 할당
        max_animal = ''
        max_animal_count = 0
        # 동물 종의 리스트 생성
        animal_list = list(animal_map.keys())
        # 리스트를 순회하며 각 동물 종의 개체 수를 딕셔너리에서 찾고, 
        # 현재 max_animal보다 개체 수가 많으면 새로운 max_animal로 할당
        for animal in animal_list:
            if animal_map.get(animal) > max_animal_count:
                max_animal = animal
                max_animal_count = animal_map.get(animal)
        # 가장 개체 수가 많은 동물 종 이름 반환
        return max_animal
    # 빈 딕셔너리일 경우 None 반환
    else:
        return None

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(find_most_populated({"lion": 5, "tiger": 3, "elephant": 10}))  # 예시: "elephant"
print(find_most_populated({}))                                       # None
print(find_most_populated({"wolf": 4, "wolfdog": 4, "hyena": 4}))     # "wolf"
#####################################################
