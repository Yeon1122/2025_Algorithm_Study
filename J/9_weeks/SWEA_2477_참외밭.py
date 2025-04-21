'''
3줄요약

방향 하나 있는거 기준값으로
면적 = 하나방향값 * 앞뒤 값 중 더 긴 값 - 
긴 거 앞뒤 값 중 더 큰값이 다음 값이면
    i = 긴값 + 1 번째

마지막 값이면
    i = 긴값 - 5 번째

왜냐면 6각형이라 반시계방향으로 돌면 순서가 그렇게 됨.

참외 수 = K * 면적

1 동
2 서
3 남
4 북

#################
1. 입력값
K
melon = []

'''

K = int(input())
melon = []

for i in range(6):
    d, l = map(int, input().split())
    melon.append((d,l))
    melonl = max(melon, key=lambda x: x[i][1]) #왜안돼,,,
    print(melonl)
#     for i in range(4):

#         if                  # i 개수가 1개일때 << 큰사각형의 세로임
#                             # [i][1] 길이가 제일 클 때 << 큰사각형의 가로임
#         melonl = melon[][]  # 큰사각형세로 좌 우 길이비교 후 다음값 혹은 마지막값 선택
#         melonr = melon[][]
#         s_melonl = melon[][]
#         s_melonr = melon[][]

# place = melonl * melonr - s_melonl * s_melonr

# ans = K * place

# print(ans)