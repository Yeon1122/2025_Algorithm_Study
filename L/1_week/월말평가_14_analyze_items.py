############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 set, sum 등 사용 시 감점

def analyze_items(items_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result_list = []
    sum1 = 0
    sum2 = 0

    
    #중복 제거
    if bool(items_list):
        for item in items_list:
            if item not in result_list:
                    result_list.append(item)

    #양수와 음수의 합
    for item in result_list:
        if type(item) is int:
            if item > 0:
                sum1 += item
            elif item < 0:
                sum2 += item

    return(f'({result_list}, ({sum1}, {sum2}))')

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
# ##제출##
# def analyze_items(items_list):
#     pass
#     # 여기에 코드를 작성하여 함수를 완성합니다.
#     result_list = list()
#     sum1 = 0
#     sum2 = 0
    
#     if bool(items_list) == False:
#         result_list = []
#     else:
#         result_list = list(set(items_list))
    
#     for item in result_list:
#         if type(item) != 'int':
#             result_list.remove(item)

#     #음수들의 합
#     for item in result_list:
#         if item < 0:
#             sum1 += item

#     #양수들의 합
#     for item in result_list:
#         if item > 0:
#             sum2 += item

#     return result_list
# #####################################################