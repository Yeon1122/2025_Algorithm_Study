# 40분 소요

# # 별 : 4
# 동그라미 : 3
# 네모 : 2
# 세모 : 1

# 4       3321    A OK
# 24321   4331    B 
##43221     
##4331
# 3211    2321    B 
##3211
##3221
# 4321    432     A
##4321
##432
# 44231   42413   D
##44321
##44321

# 내림차순 정렬해서 한 칸씩 비교
# 최댓값 빈도 비교해서 큰쪽 승리
# 최댓값 빈도 똑같다면 그 다음 최댓값 빈도 비교해서 큰쪽 승리
# while로 

R = int(input())
for rc in range (1, R+1):
    r_a = list(map(int, input().split()))
    r_b = list(map(int, input().split()))
    a = r_a[0]      # a 그림 총 갯수
    b = r_b[0]      # b 그림 총 갯수
    a_pocket = r_a[1:]
    b_pocket = r_b[1:]
    if max(a_pocket) > max(b_pocket):
        result = "A"
    elif max(b_pocket) > max(a_pocket):
        result = "B"
    else:     # 최댓값 빈도 똑같을때
        sorted_a = sorted(a_pocket, reverse=True) # 내림차순 정렬
        sorted_b = sorted(b_pocket, reverse=True)
        # 두 정렬중에서 길이 긴것까지 반복하며 크기비교
        max_len = max(len(sorted_a), len(sorted_b)) 
        for i in range(max_len):
            if sorted_a[i] > sorted_b[i]:
                result = "A"
            elif sorted_a[i] < sorted_b[i]:
                result = "B"
            elif sorted_a[i] == sorted_b[i]:
                result = "D"
    print(result)
