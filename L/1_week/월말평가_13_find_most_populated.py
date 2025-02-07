############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def find_most_populated(animal_map):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    if bool(animal_map) == False:
        return None

    else:
        max_value = 0
        max_key = str()

        for key in animal_map.keys():
            if animal_map[key] > max_value:
                max_value = animal_map[key]
                max_key = key
        return(f'"{max_key}"')


            
    

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
##제출
def find_most_populated(animal_map):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 만약 빈 딕셔너리면 None를 반환한다.
    if bool(animal_map) == False:
        return None
    # 가장 개체 수가 많은 동물의 수를 반환한다. (동물의 이름을 반환하는 방법을 찾지 못함.)
    else:
        return max(animal_map.values())
#####################################################