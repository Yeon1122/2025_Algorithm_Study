T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    x, y = 99, 0
    for col in range(100):
        if data[99][col] == 2:
            y = col
            break
    while x > 0:
        if y > 0 and data[x][y - 1] == 1:
            while y > 0 and data[x][y - 1] == 1:
                y -= 1
        elif y < 99 and data[x][y + 1] == 1:
            while y < 99 and data[x][y + 1] == 1:
                y += 1
        x -= 1
    print(f"#{test_case} {y}")