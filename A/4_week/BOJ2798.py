'''
N : 카드의 개수
M : M을 넘지않는 정수

구조
1. N, M 입력
2. 카드 리스트 입력

3. 주어진 수 3개를 합해서 최대값을 찾는데, M을 넘지 않게 한다.
for
    for
        for
    로 중복되지 않으면서 M을 넘지않는 max_sum 도출
'''
N, M = map(int,input().split())
card_list = list(map(int,input().split()))
result = 0
for i in range(N-2):
    max_sum = 0
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            max_sum = card_list[i] + card_list[j] + card_list[k]
            if max_sum <= M:
                result = max(result, max_sum)
print(result)