############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 sum, len, min, max, sorted 또는 리스트 sort 메서드 사용 시 감점

def analyze_likes(weekly_like_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    sum_list = 0
    size_list = 7
    min_list = max_list = weekly_like_list[0]

    for number in weekly_like_list:
        sum_list += number

        if number < min_list:
            min_list = number
        
        if number > max_list:
            max_list = number
    
    return(sum_list/size_list, max_list-min_list)
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
analyze_likes([2, 5, 3, 8, 0, 10, 4])
# 1) 평균 = (2 + 5 + 3 + 8 + 0 + 10 + 4) / 7
#    = 32 / 7 ≈ 4.5714...
# 2) 최소=0, 최대=10, 차이=10
# 결과: (4.5714..., 10)
print(analyze_likes([2, 5, 3, 8, 0, 10, 4]))  # 예시: (4.5714..., 10)
print(analyze_likes([7, 7, 7, 7, 7, 7, 7]))   # (7.0, 0)

#####################################################
# ##제출##    
# def analyze_likes(weekly_like_list):   
#     # 7일간 좋아요 합계를 넣을 변수 total
#     total = 0
    
#     # 리스트를 순회하면서 전체의 합을 구하고 7일간 데이터이니 7로 나눠 평균 구해 avg에 저장.
#     # float()를 통해 실수로 변환
#     for like in weekly_like_list:
#         total += like
#         count = 7
#         avg = float(total/count)
    
#     # 가장 적은 좋아요 수를 저장하기 위한 변수 min
#     # 리스트를 순회하면서 첫번째 값보다 작은 값이 있으면 min에 저장
#     min = weekly_like_list[0]
#     for like in weekly_like_list:
#         if min > like:
#             min = like
#         else:
#             continue

#     # 가장 많은 좋아요 수를 저장하기 위한 변수 max
#     # 리스트를 순회하면서 첫번째 값보다 큰 값이 있으면 max에 저장        
#     max = weekly_like_list[0]        
#     for like in weekly_like_list:   
#         if max < like:
#             max = like
#         else:
#             continue

#     # 일주일의 총 좋아요 평균인 avg와 가장 많은 좋아요 수와 가장 적은 좋아요 수의 차이(max-min)을 반환        
#     return(avg, max-min) 
    

# # 추가 테스트를 위한 코드 작성 가능
# # 예) print(함수명(인자))
# #####################################################
# # 아래 코드를 삭제하는 경우
# # 모든 책임은 삭제한 본인에게 있습니다.
# ############## 테스트 코드 삭제 금지 #################
# analyze_likes([2, 5, 3, 8, 0, 10, 4])
# # 1) 평균 = (2 + 5 + 3 + 8 + 0 + 10 + 4) / 7
# #    = 32 / 7 ≈ 4.5714...
# # 2) 최소=0, 최대=10, 차이=10
# # 결과: (4.5714..., 10)
# print(analyze_likes([2, 5, 3, 8, 0, 10, 4]))  # 예시: (4.5714..., 10)
# print(analyze_likes([7, 7, 7, 7, 7, 7, 7]))   # (7.0, 0)

# #####################################################
