'''
# 입력 데이터
W,H : 가로, 세로
N : 상점의 갯수
N개 만큼 받기(상점) # 1 : 북 , 2 : 남 , 3 : 서, 4 : 동
내 위치
dir = {1 : 0, 2 : W, 3 : 0 , 4 : H)

#구조
북동, 서동 인 경우에만 case 구별 해주면 됨 나머지 절대값으로 뺀 값

상점의 개수 만큼 돌면서
    a,b


1. 그래프가 반대 인 경우
    전체 길이 구하고, 좌표 다 더하고 더 짧은거 구하면 됨
2. 그래프가 반대가 아닌 경우
    두 좌표를 빼서 더한다.



0,4 (1 4)
5,3 (2 3)
12

2,0 (3 2)
5,3 (2 3)
6

5,8 (2 8)
5,3 (2 3)
5

'''

W,H = map(int,input().split())
N = int(input())
graph = []
border = 2*(W+H)
sum = 0
for i in range(N+1):
    a, b = map(int,input().split())

    if a == 1:
        c = [0, b]
    elif a == 2:
        c = [H, b]
    elif a == 3:
        c = [b, 0]
    else:
        c = [b, W]

    if i == N:
        graph.insert(0, c)
        break
    graph.append(c)

for k in range(1,N+1):
    if abs(graph[0][0] - graph[k][0]) == H or abs(graph[0][1] - graph[k][1]) == W:
        a1 = (abs(graph[0][0] + graph[k][0]) + abs(graph[0][1] + graph[k][1]))
        a2 = border - a1

        min_sum = min(a1,a2)
        sum += min_sum
        continue


    min_sum = (abs(graph[0][0] - graph[k][0]) + abs(graph[0][1] - graph[k][1]))


    sum += min_sum

print(sum)






