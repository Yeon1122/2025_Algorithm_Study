from itertools import permutations
T = int(input())
for test_case in range(1, T+1):
    N=int(input())
    cal_list_num = list(map(int, input().split()))

    cal_list = []
    # print(cal_list_num, sum(cal_list_num))
    for i in range(len(cal_list_num)):
        if i == 0:
            for j in range(cal_list_num[i]):
                cal_list.append('+')
        elif i == 1:
            for j in range(cal_list_num[i]):
                cal_list.append('-')
        elif i == 2:
            for j in range(cal_list_num[i]):
                cal_list.append('*')
        else:
            for j in range(cal_list_num[i]):
                cal_list.append('/')

    # print(cal_list)
    perm_list = []
    for perm in set(permutations(cal_list, N-1)):
        perm_list.append(perm)

    # print(perm_list)

    nums = list(map(int, input().split()))
    # print(nums)

    max_num = float('-inf')
    min_num = float('inf')


    for k in range(len(perm_list)):
        # print()
        num = 0
        num_copy = nums[:]
        num += num_copy.pop(0)
        # print(num, num_copy)
        for i in range(len(num_copy)):
            if perm_list[k][i] == '+':
                # print('+')
                num += num_copy[i]
            elif perm_list[k][i] == '-':
                # print('-')
                num -= num_copy[i]
            elif perm_list[k][i] == '*':
                # print('*')
                num *= num_copy[i]
            else:
                # print('/')
                num /= num_copy[i]
                num = int(num)
            # print(num)



            # print(num)

        if max_num<num:
            max_num = num
        if min_num>num:
            min_num = num

            # print(max_num, min_num)

    print(f'#{test_case} {max_num-(min_num)}')
