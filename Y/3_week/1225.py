T = 10
for tc in range(1, T+1):
    test_case = int(input())
    nums = list(map(int, input().split()))
    N = len(nums)

    while nums[N-1] > 0: #0과 같거나 작을 때 멈춰야함 => 0보다 클 때 무한 루프
        # 한 사이클에서 하나씩 뺄 때마다 뺄 값이 하나씩 늘어남, 사이클 한 번 돌면 초기화
        cnt = 0
        for i in range(5):
            cnt += 1
            num = nums.pop(0) #nums의 0번째 pop => num에 할당
            num -= cnt #늘어난 값 추가해주기
            # print(nums)
            nums.append(num)
            if nums[N-1] <= 0:
                nums[N-1] = 0
                break
    print(f'#{test_case}', *nums)



