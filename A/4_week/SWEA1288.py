'''
#입력 데이터
T : tc
N : 숫자
sheep set 받을 변수


#구조
while을 돌면서 배수 계속 하면서 돌기
set함수가 10이 되면 break


'''

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    sheep = set()
    k = 1
    while len(sheep) < 10:
        a = N * k
        b = str(a)

        for i in b:
            sheep.add(i)

        k += 1

    print(f'#{tc} {a}')

