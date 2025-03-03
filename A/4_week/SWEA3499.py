'''
퍼펙트셔플

# 입력 데이터
T : 테스트 케이스
N : 카드 갯수
data = input().split()

# 구조
입력 데이터를 받아서 번갈아 가면서 나오게 하면 되는데
리스트로 받아서 그냥 홀수번 째, 짝수번 째 2번 돌면 끝일듯
데이터를 반으로 나누고

'''

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(input().split())
    if N % 2 == 0:
        length = N//2
    else:
        length = N//2 + 1

    data1 = []
    data2 = []
    ans = []
    for i in range(length):
        data1.append(data[i])

    for j in range(length,N):
        data2.append(data[j])

    if N % 2 == 0:
        for k in range(N // 2):
            ans.append(data1[k])
            ans.append(data2[k])
    else:
        for k in range(N // 2):
            ans.append(data1[k])
            ans.append(data2[k])
        ans.append(data1[k+1])

    print(f'#{tc}', *ans)
