'''
색종이 문제랑 똑같이 1로 바꿔서 풀면 되지 않을까?
일단 가로 세로의 길이가 정해져있고, 좌표가 주어지니 거기에 맞춰서 하면 될 것 같다.

'''

xy = [[0] *100 for _ in range(100)]
coor = []
sum = 0

for i in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    c = [x1, y1, x2, y2]
    coor.append(c)


for i in range(len(coor)):
    for k in range(coor[i][0], coor[i][2]):
        for n in range(coor[i][1], coor[i][3]):
            xy[k][n] = 1


for j in range(len(xy)):
    sum += xy[j].count(1)

print(sum)