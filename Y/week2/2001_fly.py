T=int(input())
N, M =0, 0

for test_case in range(1, T+1):
    #변수
    N, M  = list(map(int, input().split()))
    fly_list = [list(map(int,input().split())) for _ in range(N)]
    fly_sum_a = -1
    fly_sum = 0


    for i in range(N-M+1):
        for j in range(N-M+1):

            fly_sum = 0
            for r in range(M):
                for c in range(M):
                    fly_sum += fly_list[i+r][j+c]

            if fly_sum_a < fly_sum:
                fly_sum_a = fly_sum

    print(f'#{test_case} {fly_sum_a}')

    ################################################

T=int(input())
N, M =0, 0

for test_case in range(1, T+1):
    #변수
    N, M  = list(map(int, input().split()))
    fly_list = [list(map(int,input().split())) for _ in range(N)]
    fly_sum = -1

    def catch_fly(fly_list, r, c):
        catch_sum = 0
        for i in range(M):
            for j in range(M):
                catch_sum += fly_list[r+i][c+j]
        return catch_sum


    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_sum = catch_fly(fly_list,i,j)

            if fly_sum < temp_sum:
                fly_sum = temp_sum

    print(f'#{test_case} {fly_sum}')
    
