sum_sq = 0
squre = [[0]*100 for _ in range(101)]
# print(squre)
for a in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            squre[i][j] = 1

for i in range(len(squre)):
    for j in range(len(squre)-1):
        sum_sq += squre[i][j]

print(sum_sq)