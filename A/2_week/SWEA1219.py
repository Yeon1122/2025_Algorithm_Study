'''
A > B 를 가면서 길을 찾는 프로그램
0이 시작 인덱스 99가 도착 인덱스라고 하자.
유향이므로 양방향으로 대입하지말고, 한 곳만 생각하면서 진행하자
길의 방향을 나타내는 [0] * 100을 사용해야 함.
visited[0] 배열도 나타내야 하나?

입력 :
1. tc Node의 갯수
2. 간선의 연결
for i in range(N):
    a, b = map(int, input().split())
    [i*2] [i*2+1]

구조 :
DFS를 기본 구조로  99에 도착하면 끝나도록 설정하면 될 듯?
다 끝나고 visited 99 에 1이 찍혀있으면 or 찍으면 으로 설계하면 될 것 같다.
'''
for test_case in range(1, 11):
    tc, N = map(int,input().split()) # tc와 Node
    road_graph = list(map(int,input().split()))
    visited = [0] * 100
    road = [[] for _ in range(100)]
    for i in range(N):
        a, b = road_graph[i*2] , road_graph[i*2+1]

        road[a].append(b)


    def dfs(v):



        visited[v] = 1

        for i in road[v]:
            if not visited[i]:
                dfs(i)
    dfs(0)

    if visited[99] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
