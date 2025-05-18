'''
2
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0

#1 2
#2 6

1. 행 방향 세주기

0 마주치면
길이가 K에 다다랐는지 확인
    다다랐다면, count +1
    아니라면, 종료

행 다 돌고 나서
길이가 K에 다다랐는지 확인
    다다랐다면, count +1


2. 열 방향 세주기
상동

'''

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    txt = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    #1. 행방향 글자세기
    for i in range(N):
        length = 0
        for j in range(N):
            if txt[i][j] == 1:
                length += 1
            else:
                if length == K:
                    count += 1
                length = 0

        if length == K:
            count += 1

    #2. 열방향 글자세기
    for j in range(N):
        length = 0
        for i in range(N):
            if txt[i][j] == 1:
                length += 1
            else:
                if length == K:
                    count += 1
                length = 0

        if length == K:
            count += 1

    # print(count)
   
    print(f'#{tc} {count}')