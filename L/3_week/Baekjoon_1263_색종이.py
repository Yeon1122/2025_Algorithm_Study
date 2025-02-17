N = int(input()) #색종이의 수
location = [list(map(int,input().split())) for _ in range(N)] #색종이 붙인 위치
max_x = max_y = count = 0

for x, y in location:
    max_x = max(max_x, x + 10)
    max_y = max(max_y, y + 10)

matrix = [[0] * max_x for _ in range(max_y)]

for x, y in location:
    for i in range(10):
        for j in range(10):
            matrix[y+i][x+j] = 1

for i in range(max_y):
    for j in range(max_x):
        if matrix[i][j] == 1:
            count += 1

print(count)