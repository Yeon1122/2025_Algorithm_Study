# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cards = [0] + input().split()
#     card1 = []
#     card2 = []
#     result = []

#     for i in range(1, N):
#         if i % 2 == 1:
#             card1 += cards[i]
#         if i % 2 == 0:
#             card2 += cards[i]

#     if N % 2 == 0:
#         m = N // 2
#         for i in range(1, m):
#             result += card1[i]
#             result += card2[i]
#     else:
#         m = N // 2
#         for i in range(1, m):
#             result += card1[i]
#             result += card2[i]
#         result += card1[m+1]

#     print(f'#{tc} {result}')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input().split()

    m = (N + 1) // 2
    card1 = cards[:m]
    card2 = cards[m:]

    result = []

    for i in range(len(card2)):
        result.append(card1[i])
        result.append(card2[i])

    if len(card1) > len(card2):
        result.append(card1[-1])

    print(f'#{tc} {" ".join(result)}')