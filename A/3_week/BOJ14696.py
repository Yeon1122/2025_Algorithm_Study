'''
입력:
라운드 수 N
그림의 총 개수 나오고 뒤에 가지고 있는 값
출력:
승리 한 사람의 알파벳 무승부 D

4의 개수 , 3의 개수, 2의 개수, 1의 개수를 카운팅해서 비교하면 끝

'''

T = int(input())
for tc in range(1, T+1):
    A_list = list(map(int,input().split()))
    B_list = list(map(int,input().split()))

    for i in range(4,0,-1):
        if A_list[1::].count(i) > B_list[1::].count(i):
            print('A')
            break
        elif A_list[1::].count(i) < B_list[1::].count(i):
            print('B')
            break
    else:
        print('D')