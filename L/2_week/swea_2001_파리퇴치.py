#파리 퇴치
# [압력]
T = int(input())  #테스트 케이스의 개수

for test_case in range(1, T+1): #테스트 케이스만큼 반복
    N,M = map(int,input().split()) #N: 전체 배열의 크기 M: 파리채의 크기
    arr = [list(map(int,input().split())) for _ in range(N)]

# [처리]
    # **변수**
    max_flies = 0 #최대 파리 수
    
    # **식**
    #전체 요소를 돌면서
    for i in range(N-M+1):
        for j in range(N-M+1):
            arr[i][j]
            sum_tem = 0      
    #기준점에서 0~M 0~M 범위내에 있는 요소들의 합
            for a in range(M):
                for b in range(M):
                    sum_tem += arr[i+a][j+b]
    #최대 파리 수보다 요소들의 합이 크다면 최대 파리 수에 요소들의 합 할당
            if max_flies < sum_tem:
                max_flies = sum_tem

# [출력]
    print(f'#{test_case} {max_flies}')
    
####
#강사님 풀이1#
T = int(input())
N, M = 0, 0

def catch_fly(files, r, c):
    catch_sum = 0
    for i in range(M):
        for j in range(M):
            catch_sum += files[r+i][c+j]
    
    return catch_sum


for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = -1
    files = [list(map(int,input().split())) for _ in range(N)]
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_sum = catch_fly(files, i, j)
            if answer < temp_sum:
                answer = temp_sum 

    print(f'#{tc} {answer}')
    
###
#강사님 풀이2#
T = int(input())
N, M = 0, 0

for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = -1
    files = [list(map(int,input().split())) for _ in range(N)]
    
    prefix_sum = [[0]*(N+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + prefix_sum[i-1][j-1] + files[i-1][j-1]
    
    for i in range(M, N+1):
        for j in range(M, N+1):
            temp_sum = prefix_sum[i][j] - prefix_sum[i-M][j] - prefix_sum[i][j-M] + prefix_sum[i-M][j-M]
            if answer < temp_sum:
                answer = temp_sum
                
    print(f'#{tc} {answer}')