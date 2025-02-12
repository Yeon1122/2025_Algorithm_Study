T = int(input())
for testcase in range(1, T+1):
    count = 0
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    i = 0
    while A != B:
        if A[i] != B[i]:
            for j in range(i, N):
                A[j] = 1 - A[j]                 # A[i] = A[i] % 2
            count += 1
        i = i + 1
    
    print(f"#{testcase} {count}")

    # while 써서 AB 같을때까지 돌리기
    # for 로 range i 부터 N 까지 돌리기
    # for 안에 if로 A[i] = 1 - A[i], count += 1, i = i + 1
    # i, i 두개 쓰이니까 하나 j로 바꾸기


    # N, N+1 헷갈리지 않기
    # 변수 할당 겹치는거 아닌지 보기