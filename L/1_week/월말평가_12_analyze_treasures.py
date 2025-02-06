############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def analyze_treasures(treasure_list, threshold):
    pass

    count_dic = {}
    over_threshold = 0

    for treasure in treasure_list:
        if treasure in count_dic:
            count_dic[treasure] += 1
        else:
            count_dic[treasure] = 1
    
    for v in count_dic.values():
        if v > threshold:
            over_threshold += 1
    
    return(count_dic, over_threshold)


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
# ##제출##
# def analyze_treasures(treasure_list, threshold):
#     pass
#     # 여기에 코드를 작성하여 함수를 완성합니다.

#     # {보물이름: 개수} 형태를 담을 딕셔너리 treasure_dic 변수
#     treasure_dic = {}
#     # 임계값을 넘는 보물 세는 over_count 변수수
#     over_count = 0

#     # 전체 treasure_list 리스트를 순환하면서
#     for i in range(len(treasure_list)-1):
#         #제일 첫번째 요소인 treasure_list[0]은 1개 count 해주고
#         treasure_dic[treasure_list[0]] = 1
#         # 없으면 키:값 으로 만들어주고
#         if treasure_list[i+1] != treasure_list[i]:
#             treasure_dic[treasure_list[i+1]] = 1
#         # 있으면 값에 1을 더해준다
#         else:
#             treasure_dic[treasure_list[i]] += 1

#     #임계값을 이상을 초과하는 보물 종류 수
        
#         values_list = treasure_dic.values()

#         #임계값보다 value가 크면 over_count에 1을 더한다.
#         for value in values_list:
#             if value > threshold:
#                 over_count += 1

#     #보물이 종류별로 몇개씩 있는지 알 수 있는 딕셔너리와, 임계값 이상 보물의 수를 반환한다.
#     return treasure_dic, over_count