def snail_rotate(n):
    matrix = [[0] * n for _ in range(n)]
    
    #오른쪽, 아래, 왼족, 위
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    r = 0
    c = 0 
    dir = 0
    
    for num in range(1, n * n + 1):
        matrix[r][c] = num
        
        #다음 위치
        nr, nc = r + delta[dir][0], c + delta[dir][1]

        #다음 위치 나아가는 방향 dir 정하기
        if nr >= n or nc >= n or matrix[nr][nc] != 0:
            dir = (dir + 1) % 4
            #정한 dir 다음 위치에 넣기
            nr, nc = r + delta[dir][0], c + delta[dir][1]
        #다음 위치 좌표 넣기
        r, c = nr, nc
    
    return matrix

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    answer = snail_rotate(N)
    
    print(f'#{tc}')
    for row in answer:
        print(" ".join(map(str, row)))