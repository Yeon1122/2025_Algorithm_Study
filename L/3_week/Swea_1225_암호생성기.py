#암호생성기

T = 10

for tc in range(1, T+1):
    input()
    numbers = list(map(int,input().split()))

    while True:
        for i in range(1,6):
            last = max(0, numbers.pop(0) - i)
            numbers.append(last)

            if last == 0:
                break

        if last == 0:
            break


    print(f'#{tc}', *numbers)