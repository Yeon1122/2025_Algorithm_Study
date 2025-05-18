'''
3
3 3
0 1 0
0 1 0
0 1 0
3 3
0 1 0
1 1 1
0 0 0
8 8
0 0 0 0 0 0 1 0
0 1 1 1 1 0 1 0
0 0 0 0 0 0 1 0
0 0 0 1 0 0 1 0
0 0 0 1 0 0 1 0
0 1 1 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

#1 3
#2 3
#3 6

구조물 있으면 1
없으면 0
1*1은 노이즈 이므로, 최대길이 1이면 0으로 침.

가장 긴 길이 : max_val
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    tower = [list(map(int, input().split())) for _ in range(N)]
    length = 0
    max_val = 0

    #1. 행탐색
    for i in range(N):
        length = 0
        for j in range(M):
            if tower[i][j] == 1:
                length += 1               
            else:
                length = 0
            # print(length)
            if max_val< length:
                max_val = length
        
    
        if max_val == 1:
            max_val = 0

    #2. 열탐색
    for j in range(M):
        length = 0
        for i in range(N):
            if tower[i][j] == 1:
                length += 1               
            else:
                length = 0
            # print(length)
            if max_val< length:
                max_val = length
        
    
        if max_val == 1:
            max_val = 0
    print("답", max_val)

    # print(max_val)
            
    # print(tower)
    # print(f'#{tc}')