'''
델타 함수를 이용하고
90도 돌리면 된다.

출력 결과값에 +1을 해주자

'''

C, R = map(int,input().split())
seat = [[0]*R for _ in range(C)]
K = int(input())

di = [0,1,0,-1] # 우 하 좌 상
dj = [1,0,-1,0]
dir = 0
seat_num = 1

i = 0
j = 0

a = b = -1
while seat_num <= C*R:

    seat[i][j] = seat_num

    if seat_num == K:
        a, b = i+1, j+1

    seat_num += 1

    ni = i + di[dir]
    nj = j + dj[dir]

    if not (0 <= ni < C and 0 <= nj < R and seat[ni][nj] == 0):
        dir = (dir + 1) % 4
        ni = i + di[dir]
        nj = j + dj[dir]

    i = ni
    j = nj


if a == -1 and b == -1:
    print(0)
else:
    print(a, b)