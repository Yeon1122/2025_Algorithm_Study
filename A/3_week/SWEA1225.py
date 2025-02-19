from collections import deque

for tc in range(1,11):
    T = int(input())
    password = list(map(int,input().split()))
    q = deque()
    for i in range(len(password)):
        q.append(password[i])

    while True:

        if q[7] == 0:
            break


        for i in range(1,6):
            a = q.popleft()
            a = a - i
            if a <= 0:
                a = 0
                q.append(a)
                break
            else:
                q.append(a)

    print(f'#{tc}', *q)
