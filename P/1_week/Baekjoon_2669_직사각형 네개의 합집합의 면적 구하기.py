# 2669 직사각형 네개의 합집합의 면적 구하기 / 30분
coordinate_set = set()
N = 4
for square in range(N):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    for i in range(x_1, x_2):
        for j in range(y_1, y_2):
            coordinate_set.add((i, j))
print(len(coordinate_set))
