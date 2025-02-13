'''
간단하게 갯수를 세어주는 문제
입력 :
N : 라운드 수
A가 내는 딱지에 나온 그림의 총 개수 a / 각 수에 맞는 모양 (별 : 4, 동그라미 : 3 , 네모 : 2 , 세모 : 1)
star , circle, sq, tri

구조 :
N이 라운드 수 이므로 testcase를 도는 형식으로 하면 좋을 것 같고
입력을 2개 받고 출력하는 형식의 tc를 돌면 될듯

for문에서 if문을 이용해서 각 숫자에 맞게 배열하면 될듯

'''

N = int(input())
for rnd in range(N):
    lst_a = list(map(int,input().split()))
    lst_b = list(map(int,input().split())) # 0번 인덱스는 개수, 그 뒤 인덱스부터는 모양

    for i in [4,3,2,1]:
        if lst_a[1:].count(i) > lst_b[1:].count(i):
            print('A')
            break
        elif lst_a[1:].count(i) < lst_b[1:].count(i):
            print('B')
            break
    else: # 같은 경우 : for - else를 이용
        print('D')
# count() 를 안 쓰는 방법도 생각해보면 좋을듯




