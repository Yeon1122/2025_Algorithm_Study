grid = [[0] * 101 for _ in range(101)]       # 100x100
for _ in range(4):
    data = input()
    x1, y1, x2, y2 = map(int, data.split())  # 네 개의 좌표 값
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] = 1
total_area = 0
for i in range(101):
    for j in range(101):
        if grid[i][j] == 1:
            total_area += 1
print(total_area)

