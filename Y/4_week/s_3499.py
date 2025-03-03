#############################
# 전역변수 T
# N:카드 수
# card : 카드리스트(구분자 ' ')
# 
# 1. 카드 수의 절반을 알아야함
#   -> 만약 홀수인 경우 올림
#   -> 더 큰 수를 변수에 저장(h), 나머지 덱은 전체 - 큰 수
# 2. 카드 리스트를 절반으로 나눠야함
#   -> 슬라이싱을 사용하면 리스트를 두 개로 나눌 수 있을 듯
# 3. 두 리스트를 번갈아가면서 섞어주기
#   ->번갈아가면서 넣어줄 빈 리스트 필요(shuffle)
#   ->만약 리스트의 길이가 둘이 다른 경우(한 쪽이 +1만큼 더 큰 경우)
#   -> 분기 지정해주기 (if)#
#   1안) 순서를 지정해주기 위해서 h만큼 반복
#        만약 리스트의 길이가 둘이 다른 경우 i가 h-2일때까지 돌아주기
# 		->긴 쪽의 인덱스 = h-1, 짧은 쪽의 인덱스 h-1 => 인덱스 에러 방지
#   2안)pop을 활용해서 card1가 없는 경우까지 돌아주기
#		card2가 없어지기 전까지 돌아주고 없어지면 card2 없이 card1만 추가
# #


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    shuffle = []

    if N%2 == 1:
        h = N//2+1
    else:
        h = N//2

    cards1 = cards[:h]
    cards2 = cards[h:]

    # print(cards1, cards2)
    # for i in range(h):
    #     if len(cards1) !=len(cards2):
    #         if i == h-2:
    #             shuffle.append(cards1[i])
    #             shuffle.append(cards2[i])
    #             shuffle.append(cards1[i+1])
    #             break
    #         else:  
    #             shuffle.append(cards1[i])
    #             shuffle.append(cards2[i])
    #     else:
    #         shuffle.append(cards1[i])
    #         shuffle.append(cards2[i])

    while cards1:
        if len(cards2) != 0:
            shuffle.append(cards1.pop(0))
            shuffle.append(cards2.pop(0))
        else:
            shuffle.append(cards1.pop(0))

    print(f'#{test_case}', *shuffle)

