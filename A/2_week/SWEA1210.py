'''
입력 데이터 :
테스트 케이스(tc)
사다리 모양(2차원 리스트로 받아야할듯)

변수 데이터 :
사다리 모양 빈 리스트

출력 데이터 :
몇 번쨰 인덱스에서 출발해야 [9][9] 에 도착이 되는지 == 2 라는 숫자가 출력되면.

구조
for문으로 빈 인덱스를 넣어야 할거같은데

[i][j]인 2차원 리스트를 가지게 되고,
j값이 계속 증가하다가 i값에서 값 측정이 되면 i와j가 같이 바뀌는 형태


j가 9인 경우 멈춰야 함
[i][j] = [9][9]인 경우 시작한 곳이 답

i가 세로줄 j가 가로줄이에요

처음에 0번 인덱스에서 시작 할 j 설정
i값을 늘리며 양 옆 j에 값이 있다면 +-1을 해줘야 함
2가 도출되면 break


구조
ladder[i][j]
첫 줄에서 시작하는 곳을 찾아
인덱스[i]를 계속 늘려가야함. j는 고정하고 근데, j가 값이 변경되면 그때 이동임
[j][i]

i+1 == 1 인것이 발견되면 계속 더하는 방향으로 넘어가야함. 그리고 j값이 고정이되면서 넘어가야함
i+1 == 0 임이 발견되면 j값이 1더해지면 됨.

'''

for i in range(10):
    tc = int(input())

    ladder = []
    start_point = []
    for i in range(100):
        ladder.append(list(map(int, input().split())))


    # print(ladder)
    # print(len(ladder))

    # for i in range(100):
        ladder[i].insert(0,0)
        ladder[i].insert(101,0)
    # print(ladder)
    # print(len(ladder[0]))


    for i in range(101):
        if ladder[0][i] == 1:
            start = i
            x=0
            y=i
            while x < 99:

                judge = 0 # 0인 경우 초기화 1인 경우 왼쪽 2인 경우 오른쪽

                while judge != 1 and ladder[x][y+1] == 1:
                    y += 1
                    judge = 2

                while judge != 2 and ladder[x][y-1] == 1:
                    y -= 1
                    judge = 1

                judge = 0

                x += 1

                if ladder[x][y] == 2:
                    ans = start
                    break

    print(f'#{tc} {ans-1}')


        


'''
for i in range(100):
    if ladder[0][i] == 1:
        start = i
        for j in range(i,100):
            if ladder[i][j] == 2:
                ans = start
                break
            if ladder[i][j+1] == 1:
                j += 1
                continue
            if ladder[i][j-1] == 1:
                j -= 1
                continue
'''
# print(ans)
