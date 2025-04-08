'''
맥주 마시면서 걸어가기

[문제이해]
맥주 한 박스에 20개 / 50미터에 한 병씩
편의점에서 빈 병 버리고 새 맥주 구입 가능
박스 맥주 20병이상 불가
거리 = x 좌표의 차이 + y 좌표의 차이(맨해튼 거리)

[입력]
t #테스트 케이스의 개수
tc #(반복)
n #편의점의 개수
start #집 위치(1개)
stop #(리스트)편의점 위치(n개)
finish #펜타포트 락 페스티벌 위치(1개)

[출력]
happy or sad

[문제 풀이]
각 거리가 1000 넘으면 안됨
'''
def cal_dist(x1,y1,x2,y2):
    distance = abs(x1-x2) + abs(y1-y2)
    return distance

def dfs(start_node):
    global result

    if start_node == n+1:
            result = 'happy'
            return

    for next_node in range(n+2):
        if graph[start_node][next_node] == 1 and not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node)

t = int(input()) #테스트 케이스의 개수
for tc in range(1, t+1): #(반복)
    n  = int(input()) #편의점의 개수
    route = []
    for _ in range(n+2):
        k = list(map(int,input().split()))
        route.append(k)
    
    result = 'sad'

    graph = [[0] * (n+2) for _ in range(n+2)] #인접행렬

    for i in range(n+2):
        for j in range(n+2):
            if cal_dist(route[i][0],route[i][1],route[j][0],route[j][1]) <= 50*20:
                graph[i][j] = 1
                graph[j][i] = 1
    
    visited = [0]*(n+2)
    visited[0] = 1
    dfs(0)

    print(result)

    

