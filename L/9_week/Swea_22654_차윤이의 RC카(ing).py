'''
차윤이의 RC카
[문제 이해]
N*N 필드

G : 이동 가능 
T : 이동 불가 나무
X : 현재 RC카의 위치
Y : RC카 이동 시키고자 하는 위치

A : 앞으로 이동
L : 왼쪽으로 90도 회전
R : 오른쪽으로 90도 회전

커맨드 주어졌을 때 목적지 도달 가능한가?

[입력]
T #테스트 케이스의 개수
t #(반복) 1, T+1
N #필드의 크기
graph #(이중리스트) N개의 줄
Q #조정 횟수
C command #(반복) 커맨드 길이 커맨드 Q번

[출력]
#t 1 or 0 (도달 가능 여부)

[문제 풀이]
'''
#상,우,하,좌
di = [0,1,0,-1]
dj = [-1,0,1,0]

def move_car(i,j,dir,cur,c_len,command_lst):
    # result = 0

    # print("move",i,j,dir,command_lst[cur],graph[i][j])

    if cur == c_len:
        print(i,j)
        print(graph[i][j])
        return
        # if graph[i][j] == 'Y':
        #     return 

    
    if command_lst[cur] == 'A':
        ni, nj = i+di[dir], j+dj[dir]
        # move_car(ni,nj,dir,cur+1,c_len,command_lst)
        if 0<=ni<N and 0<=nj<N and graph[ni][nj] != 'T':
            move_car(ni,nj,dir,cur+1,c_len,command_lst)
        else:
            move_car(i,j,dir,cur+1,c_len,command_lst)
    elif command_lst[cur] == 'L':
        if dir == 0:
            dir = 3
        else:
            dir = (dir-1)%4
        move_car(i,j,dir,cur+1,c_len,command_lst)
    elif command_lst[cur] == 'R':
        dir = (dir+1)%4
        move_car(i,j,dir,cur+1,c_len,command_lst)
        

T = int(input()) #테스트 케이스의 개수
for t in range(1, T+1): #(반복) 1, T+1
    N = int(input()) #필드의 크기
    graph = [list(map(str,input())) for _ in range(N)] #(이중리스트) N개의 줄
    Q = int(input()) #조정 횟수
    command_len = []
    command = []
    for _ in range(Q):
        C, temp_command = map(str,input().split())  #(반복) 커맨드 길이 커맨드 Q번
        command_len.append(int(C))
        command.append(list(temp_command))

    # print(command_len) #[7, 8, 12]
    # print(command) #[['R', 'R', 'A', 'A', 'L', 'A', 'A'], ['R', 'R', 'A', 'A', 'L', 'A', 'A', 'A'], ['R', 'A', 'A', 'R', 'R', 'A', 'L', 'A', 'A', 'L', 'A', 'A']]
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                start_i = i
                start_j = j

    answer = []
    for k in range(Q):
        answer.append(move_car(start_i,start_j,0,0,command_len[k],command[k]))
    
    print(answer)

