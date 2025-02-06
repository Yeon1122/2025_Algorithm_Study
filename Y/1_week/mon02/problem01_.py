############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 sum, len, min, max, sorted 또는 리스트 sort 메서드 사용 시 감점

def analyze_likes(weekly_like_list):

    #평균 좋아요, 좋아요 합계 변수
    ave_like = 0
    sum_like = 0

    #가장 많은 좋아요 수, 가장 적은 좋아요 수, 차이 반환 변수
    min_like = weekly_like_list[0]
    max_like = weekly_like_list[0]
    likes_7 = 0

    #평균 구하기
    for i in weekly_like_list:
        sum_like += i

    #최소 좋아요 구하기
        if min_like>i:
            min_like = i
    
        #최대 좋아요 구하기      
        for i in weekly_like_list:
            if max_like<i:
                max_like = i

    ave_like = sum_like/7
    
    # #최소 좋아요 구하기
    # for i in weekly_like_list:
    #     if min_like>i:
    #         min_like = i
    #     else:
    #         continue

    # #최대 좋아요 구하기      
    # for i in weekly_like_list:
    #     if max_like<i:
    #         max_like = i
    #     else:
    #         continue

    #===================

    #모든 날이 같다면 최소 == 최대, 그렇지 않다면 max-min
    if max_like == min_like:
        likes_7 = 0
    else:
        likes_7 = max_like - min_like


    return ave_like, likes_7

    # 여기에 코드를 작성하여 함수를 완성합니다.

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