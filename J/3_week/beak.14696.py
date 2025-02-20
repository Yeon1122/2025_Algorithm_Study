'''
N = 딱지놀이 총 라운드 수
a = a가 내는 딱지 그림 총 개수
b = b가 내는 딱지 그림 총 개수

별 동 네 세 = 4 3 2 1

ㄱ. a, b 비교
별 개수 다르면 별 많은 쪽 > 각 열마다 4 개수 세고, 4 많은 쪽 선택
별 동그라미 같으면 (4, 3 같으면) 
네모 많은 쪽 > 2의 개수 많은 쪽
별 동 네 같 >> 세모 (1의 개수 많은 쪽)
별 동 네 세 같으면 >> 무승부 = 'D'





'''

N = int(input())

for tc in range(1,N+1):
    a, arr_a = list(map(int, input().split()))
    b, arr_b = list(map(int, input().split()))

    list_a = [1,2,3,4]
    list_b = [1,2,3,4]

    # 별의 개수가 다른다면 많은 쪽이 이긴다
    if count(arr_a.index(4)) < count(arr_b.index(4)):
        print("B")

    # 동그라미 많은 쪽이 이긴다
    if 
        
    # 네모 많은 쪽 ,,,
    
    # 세모 ,,,

    # 무승부 ,,



    


