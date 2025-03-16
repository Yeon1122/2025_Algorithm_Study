#조합
#정해진 칼로리 이하
#가장 선호하는 햄버거 점수 높음
part = []
def comb(cnt, idx):
    global result

    prefer = 0
    calorie = 0
    for a in part:
        prefer += TK[a][0]
        calorie += TK[a][1]
    
    if calorie > L:
        return
    
    if calorie <= L:
        result = max(result,prefer)

    if cnt == N:
        return

    for i in range(idx,N):
        part.append(i)
        comb(cnt+1, i+1)
        part.pop()


T = int(input())
for tc in range(1, T+1):
    N, L = map(int,input().split()) #재료의 수, 제한 칼로리
    TK = [list(map(int,input().split())) for _ in range(N)] #재료 점수, 칼로리
    result = 0

    comb(0,0)

    print(f'#{tc} {result}')
