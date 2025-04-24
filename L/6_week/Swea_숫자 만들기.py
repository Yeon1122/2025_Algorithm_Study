def calculator(numbers, lst):
    global max_result
    global min_result
    temp = 0

    if lst[0] == 0:
        temp += numbers[0]+numbers[1]
    elif lst[0] == 1:
        temp += numbers[0]-numbers[1]
    elif lst[0] == 2:
        temp += numbers[0]*numbers[1]
    elif lst[0] == 3:  
        temp += int(numbers[0]/numbers[1])

    for i in range(1,len(lst)):
        if lst[i] == 0:
            temp += numbers[i+1]
        elif lst[i] == 1:
            temp -= numbers[i+1]
        elif lst[i] == 2:
            temp *= numbers[i+1]
        elif lst[i] == 3:  
            temp = int(temp/numbers[i+1])

    max_result = max(max_result,temp)
    min_result = min(min_result,temp)

def perm(cnt):
    if cnt == N-1:
        calculator(num, cal_list)
        # print(cal_list)
        return

    for i in range(len(cal)):
        if cal[i] != 0:
            cal_list.append(i)
            cal[i] -= 1
            perm(cnt+1)
            cal[i] += 1
            cal_list.pop()


T = int(input())
for t in range(1, T+1):
    N = int(input())
    cal = list(map(int,input().split()))
    num = list(map(int, input().split()))

    cal_list = []

    max_result = float('-inf')
    min_result = float('inf')
    
    perm(0)

    result = max_result-min_result

    print(f'#{t} {result}')

