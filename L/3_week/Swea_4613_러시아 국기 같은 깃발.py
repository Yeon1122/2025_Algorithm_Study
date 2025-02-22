#swea_4613_러시아 국기 같은 깃발

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    flag = [list(map(str,input())) for _ in range(N)]
    min_changes = N * M
                
    for i in range(1, N-1): #흰색 마지막
        for j in range(i+1, N): #파란색 마지막
            changes = 0
            for k in range(i):  # 흰색 영역
                for c in range(M):
                    if flag[k][c] != 'W':
                        changes += 1
            for k in range(i, j):  # 파란색 영역
                for c in range(M):
                    if flag[k][c] != 'B':
                        changes += 1
            for k in range(j, N):  # 빨간색 영역
                for c in range(M):
                    if flag[k][c] != 'R':
                        changes += 1
            
            min_changes = min(min_changes, changes)
        
    print(f'#{tc} {min_changes}')
            
            
            
    #지점1은 1 ~ N-3 반복문
    #지점2은 i+1 ~ N-2 반복문
    
    #a - w
    #b - B
    #c = N - a - b - R
                
            
            
            
        

    
