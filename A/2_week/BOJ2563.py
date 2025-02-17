'''
입력
색종이 수
가로 거리 / 세로 거리
색종이의 크기는 10 * 10
구조
100 * 100 2차원 리스트를 만들어서 색종이 인 곳들을 모두 1로 처리해서 1 갯수를 세면 될 듯
'''

paper = int(input())
paper_lst = []
for i in range(paper):
    a,b = map(int,input().split())
    c = [a, b]
    paper_lst.append(c)

sum = 0

entire = [[0]*100 for _ in range(100)]

for i in range(len(paper_lst)):
    x = paper_lst[i][1]
    y = paper_lst[i][0]
    for k in range(10):
        for n in range(10):
            entire[x+k][y+n] = 1

for i in range(100):
    sum += entire[i].count(1)



print(sum)

