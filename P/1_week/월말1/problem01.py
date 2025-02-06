############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 sum, len, min, max, sorted 또는 리스트 sort 메서드 사용 시 감점

def analyze_likes(weekly_like_list):
    # 일자 수와 합계를 계산하기 위한 변수에 0 할당
    day_count = 0
    sum_of_likes = 0
    # 최소값과 최대값을 찾기 위한 변수에 리스트의 첫 번째 값 할당
    min_likes = weekly_like_list[0]
    max_likes = weekly_like_list[0]
    for num in weekly_like_list:
        # 리스트를 순회하여 매일 일자 수 카운트를 1 늘리고 좋아요 수를 sum_of_likes에 합함
        day_count += 1
        sum_of_likes += num
        # 해당일의 좋아요 수가 현재의 최소값보다 작다면 새로운 min_likes로 할당
        if min_likes > num:
            min_likes = num
        # 최대값도 동일 방식으로 진행
        if max_likes < num:
            max_likes = num
    # 평균과 차이를 구하고 요구사항에 맞게 형변환
    avg = float(sum_of_likes / day_count)
    diff = int(max_likes - min_likes)
    # 평균과 차이 반환
    return avg, diff

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
