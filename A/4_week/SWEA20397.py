'''
#입력데이터
T : tc
N, M : 첫 줄의 돌의 수, 뒤집기 횟수
stone = list
for M
i, j : i 번째 돌을 두고, j개의 돌에 대해 (M 만큼 반복)


#구조
for k in range(1,j+1):
i-1 의 인덱스의 j번 반복


'''

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))
    act = []
    for _ in range(M):
        i, j = map(int,input().split())
        for k in range(1, j+1):
            if i-k-1 < 0 or i+k > N:
                break
            if stone[i-k-1] == stone[i+k-1]:
                stone[i-k-1] = 1 - stone[i-k-1]
                stone[i+k-1] = 1 - stone[i+k-1]

    print(f'#{tc}', *stone)