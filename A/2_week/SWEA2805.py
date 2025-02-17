'''
농작물 수확하기
'''
T=int(input())

for tc in range(1, 1+T):
    N = int(input())
    farm = []
    center = start = end = N//2
    sum = 0
    for crops in range(N):
        crops = list(map(int, input()))
        farm.append(crops)

    for i in range(N):
        for j in range(start,end+1):
            sum += farm[i][j]

        if i < center:
            start -= 1
            end += 1
        else:  # i >= center
            start += 1
            end -= 1
    print(f'#{tc} {sum}')