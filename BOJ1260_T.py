'''
DFS , BFS
유향 / 무향 구분을 하고
N , M , V
DFS의 결과 BFS의 결과를 출력하라

DFS와 BFS는 인접 행렬, 인접 리스트 문제 中 20% 정도 나옴
간선 정보만 주어졌을 때만 사용하지만, 그 외에는 쓸 필요가 딱히 없다.
연결 관계 -> Delta 상, 하, 좌, 우 + 좌상, 좌하, 우상, 우하 하면 연결 관계 저장 끝.

문제 조건 충족시키지 않은 것 : 방문할 수 있는 정점이 여러 개인 경우 작은 곳 부터 해라 -> for문을 이용해서 1번부터 했기 때문에
인접리스트로 해야한다면 로직이 필요하다.
'''
from collections import deque
# de = double ended

# 인접 행렬
N, M, V = map(int, input().split())
adj_matrix = [[0] * (N+1) for _ in range(N+1)] #1,2,3,4 번 인덱스를 쓸거기 때문에 사용
visited = [0]*(N+1) #1,2,3,4 에 대해서 방문했는지 체크해야 함

# v : 현재 방문하고 있는 지점 / V : 시작 지점
def dfs(v):
    visited[v] = 1
    print(v, end=" ")

    for i in range(1, N+1):
        # i지점을 방문하지 않았고
        # v(현 지점)와 i(다음 지점)이 연결 상태인 경우
        if not visited[i] and adj_matrix[v][i] == 1:
            dfs(i)
def bfs(v):
    q = deque()

    print(v, end=" ")
    visited[v] = 2
    q.append(v)

    while q:
        # q에서 뺄 때, 방문 처리 하겠다 > 그렇게 하면 안 됨
        # bfs에서 q에서 뺄 때 방문 처리를 하면 다른 인자가 추가 될 가능성이 있기 때문이다.

        cur_pos = q.popleft()
        for i in range(1, N+1):
            if visited[i] == 1 and adj_matrix[cur_pos][i] == 1:
                print(i, end=" ")
                visited[i] = 2
                q.append(i)

# 인접 행렬 입력 받아서 저장 끝
for i in range(M):
    a, b = map(int,input().split())
    adj_matrix[a][b] = 1
    adj_matrix[b][a] = 1 # 무향 그래프이므로 역과정도 같이 넣어줘야 함

dfs(V)
# 원래 였으면 방문 배열을 초기화 해줘야 함.
print()
bfs(V)
