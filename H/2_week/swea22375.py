T = int(input())
for testcase in range(1, T+1):
    count = 0
    N = int(input())                            # 숫자 하나만 정수형으로 바꿀거니까
    A = list(map(int, input().split()))         # 한 줄에 띄어쓰기로 여러개 숫자를 리스트로 변환(기준 : 띄어쓰기 - 기본split())
    B = list(map(int, input().split()))
    i = 0                                       # i(A, B 다른 숫자 위치 - 0부터 시작) 초기화
    while A != B:                               # A, B 전체가 다르면 while 시작 (같을때까지 계속 반복)
        if A[i] != B[i]:                        # i번째에서 A, B가 다르면 if 실행
            for j in range(i, N):               # i부터 N-1까지 1->0, 0->1로 바꿔주기 / j : 0, 1 바꿔주는 인덱스
                A[j] = 1 - A[j]                 # A[i] = A[i] % 2
            count += 1                          # i 자릿수 개수 바뀌어서 그 이상 모든 자리 바뀔때마다 1 카운트
        i = i + 1                               # A[i] == B[i] 가 되면 그 다음 i+1이 같아질때까지 또 돌려야하니까 위치는 while 안
    
    print(f"#{testcase} {count}")

    # while 써서 AB 같을때까지 돌리기
    # for 로 range i 부터 N 까지 돌리기
    # for 안에 if로 A[i] = 1 - A[i], count += 1, i = i + 1
    # i, i 두개 쓰이니까 하나 j로 바꾸기

    # N, N+1 헷갈리지 않기
    # 변수 할당 겹치는거 아닌지 보기