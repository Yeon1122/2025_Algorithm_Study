#################
# 전역변수 : T
# N:돌의 수 M:뒤집기 수
# #
# stones:초기상태
# i번째, j개의 돌
# 1. stone에서 i번째 돌을 찾기
# 리스트의 인덱스와 실제 돌 숫자랑 다름
# -> 실제 돌 숫자를 구해야함 (i-1)
# i번째 돌에서 j개의 돌의 값을 찾기
# -> i-1과 i+1이 같을 경우 다른 색으로 뒤집기
# -> j만큼 더할 값이 커져야함
# -> 반복문을 활용해서 숫자를 키워가기
# ->for k in range(j)
#   if stone[idx+k] == stone[idx-k]:
#       stone[idx+k] = (stone[idx+k]+1)%2
#       stone[idx-k] = (stone[idx-k]+1)%2
# 
# 
# #

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))
    for k in range(M):
        i, j = map(int, input().split())
        idx = i-1
        
        for k in range(1,j+1):
            # print(j, idx, idx+j, idx-j)
            if 0<=idx+k<N and 0<=idx-k<N:
                if stones[idx+k] == stones[idx-k]:
                    stones[idx+k] = (stones[idx+k]+1)%2
                    stones[idx-k] = (stones[idx-k]+1)%2
            else:
                break
            
    print(f'#{test_case}',*stones)