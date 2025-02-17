'''
조합을 모두 출력 한 후
그 조합에 따라서 다 계산하고
최소값 계산하면 될듯

블루가 나온 경우 화이트가 없어야 한다
레드가 나온 경우 레드만 출력해야 한다.

화이트 블루 레드 순으로 조합해야한다.
정도만 if문과 for문을 쓰면 될 듯.

Tip)
어떤 구역은 W, B, R 이다.
W와 R가 구분이 되는 지점이 중요하다.
지점 1 : 1, N-3 / 지점 2 : i+1 , N-2 /
지점 1,2를 돌리면 지점 3은 자동으로 정해짐
a + b + c = N
c = N - a - b
각 행마다 한 줄로 퉁 침

N*M
M * 1 까지 내가 화이트로 바꿔줄 수 있는거
M * 3

1
4 5
WRWRW
BWRWB
WRWRW
RWBWR

1
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
'''
T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    flag_lst = []
    cnt = 0
    min_value = float('inf')
    for _ in range(N):
        color = input()
        flag_lst.append(color)

    for w in range(N-2):
        for b in range(w+1, N-1):
            cnt = 0
            for i in range(w+1):
                cnt += M - flag_lst[i].count('W')
            for j in range(w+1, b+1):
                cnt += M - flag_lst[j].count('B')
            for k in range(b+1, N):
                cnt += M - flag_lst[k].count('R')

            min_value = min(min_value, cnt)

    print(f'#{tc} {min_value}')