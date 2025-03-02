##########################
# 1. 카드리스트에서 3개의 조합을 만들어서 조합의 합이 21이하, 최댓값일때 블랙잭#

N, M = map(int, input().split())
cards = list(map(int, input().split()))
comb_card = []
max_blackjack_sum = 0
blackjack_sum = 0

# print(N, M, cards)

def comb_blackjack(cnt, idx):
    global blackjack_sum, max_blackjack_sum
    if cnt == 3:
        # print(comb_card)
        blackjack_sum = sum(comb_card)
        if blackjack_sum<=M:
            max_blackjack_sum = max(max_blackjack_sum, blackjack_sum)
        
        return max_blackjack_sum
    else:
        for i in range(idx, N):
            comb_card.append(cards[i])
            comb_blackjack(cnt+1, i+1)
            comb_card.pop()


comb_blackjack(0,0)
print(max_blackjack_sum)
