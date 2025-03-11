from itertools import combinations

T = int(input())

def comb(cnt, i):       # 조합 - 약품 투입 경우의 수
    if cnt == min_count:
        perm(c, [], 0)
        return
    for j in range(i, D):
        c.append(combinations_list[j])
        comb(cnt + 1, j + 1)
        c.pop()
    
def perm(c, applied, cnt): # 중복순열 - 약품 투입 후 성능검사
    global result
    if cnt == len(c):
        modified_film = apply_drug(film, applied)
        if check_valid(modified_film, K):
            result = min(result, len(applied))
        return
    
    perm(c, applied + [(c[cnt], 0)], cnt + 1)
    perm(c, applied + [(c[cnt], 1)], cnt + 1)

def apply_drug(film, applied):
    modified_film = [row[:] for row in film]  # 깊은 복사
    for row, val in applied:
        modified_film[row] = [val] * W
    return modified_film

def check_valid(film, K):      # 성능검사
    for j in range(W):
        count = 1
        for i in range(1, D):
            if film[i][j] == film[i-1][j]:
                count += 1
            else:
                count = 1
            if count >= K:
                break
        else:
            return False
    return True

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    
    if check_valid(film, K):
        print(f"#{tc} 0")
        continue
    
    result = float('inf')
    combinations_list = list(range(D))
    
    for min_count in range(1, D + 1):
        c = []
        comb(0, 0)
        if result != float('inf'):
            break
    
    print(f"#{tc} {result}")