T=int(input())
for test_case in range(1, T+1):
    #변수 설정
    N=int(input())
    switch = list(map(int, input().split()))
    switch_2 = list(map(int,input().split()))
    cnt = 0
 
    for i in range(N):
        if switch[i] != switch_2[i]:
            for j in range(N-i):
                switch[i+j] = 1-switch[i+j]
            cnt += 1
 
    print(f'#{test_case} {cnt}')