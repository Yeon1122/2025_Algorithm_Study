square_location = [list(map(int,input().split())) for _ in range(4)]

max_x = 0
max_y = 0

for i in range(len(square_location)):
    for j in range(0,4,2):
        if max_x < square_location[i][j]:
            max_x = square_location[i][j]
    
    for j in range(1,4,2):
        if max_y < square_location[i][j]:
            max_y = square_location[i][j]

square_area = [[] for _ in range(max_y)]

for i in range(max_y):
    for j in range(max_x):
        square_area[i].append(i * max_x + j + 1)

set_a = []
set_b = []
set_c = []
set_d = []

for i in range(square_location[0][1],square_location[0][3]):
    for j in range(square_location[0][0],square_location[0][2]):
        set_a.append(square_area[i][j])

for i in range(square_location[1][1],square_location[1][3]):
    for j in range(square_location[1][0],square_location[1][2]):
        set_b.append(square_area[i][j])

for i in range(square_location[2][1],square_location[2][3]):
    for j in range(square_location[2][0],square_location[2][2]):
        set_c.append(square_area[i][j])

for i in range(square_location[3][1],square_location[3][3]):
    for j in range(square_location[3][0],square_location[3][2]):
        set_d.append(square_area[i][j])

set_a = set(set_a)
set_b = set(set_b)
set_c = set(set_c)
set_d = set(set_d)

set_result = (set_a | set_b | set_c | set_d)
print(len(set_result))

# Chatgpt를 통해 얻은 간결한 코드
# square_location = [list(map(int, input().split())) for _ in range(4)]

# max_x = max(x for i in square_location for x in [i[0], i[2]])
# max_y = max(y for i in square_location for y in [i[1], i[3]])

# covered_area = set()

# for x1, y1, x2, y2 in square_location:
#     for x in range(x1, x2):
#         for y in range(y1, y2):
#             covered_area.add((x, y))

# print(len(covered_area))