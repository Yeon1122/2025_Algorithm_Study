from copy import deepcopy

def calculator(idx, value):
    global max_val,min_val
    if idx == N-1:
        if max_val < value:
            max_val = value
        if min_val > value:
            min_val = value
        return
    for i in range(4):
        if equator[i]:
            if i == 0:
                value += numbers[idx + 1]
            elif i == 1:
                value -= numbers[idx + 1]
            elif i == 2:
                value *= numbers[idx + 1]
            else:
                value = int(value / numbers[idx + 1])
            equator[i] -= 1
            calculator(idx + 1, value)
            equator[i] += 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    equator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_val = -21e8
    min_val = 21e8

    calculator(0, numbers[0])

    print(f'#{tc} {max_val} {min_val}')