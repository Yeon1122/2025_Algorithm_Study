'''
키 순서

[문제이해]
1~N번까지의 학생
N명의 학생들의 키는 모두 다름

a가 b보다 작으면 a에서 b로 화살표

[입력]
N, M #학생의 수, 학생 키를 비교한 횟수
a, b #a가 b보다 작음

[출력]
자신의 키가 몇 번재인지 알 수 있는 학생들의 수

[문제 풀이]
뭔가 그래프, 트리인데....내가 몇번째인지 알고 있다를 어떻게 알지??
- 내 기준으로 나가고 들어오고
- 내가 아는 걸 기준으로 들어가면 들어가고, 나오면 나오는걸로 아는 애
'''
from collections import deque

def bfs(start, graph):
    visited = [0]*(N+1)
    q = deque()
    q.append(start)
    visited[start] = 1
    count = 0

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                q.append(next_node)
                count += 1
    return count

N, M = map(int,input().split()) #학생의 수, 학생 키를 비교한 횟수
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b) #a가 b보다 작음
    reverse_graph[b].append(a) #b가 a보다 작음

result = 0


for i in range(1, N+1):
    small = bfs(i, reverse_graph)
    big = bfs(i, graph)        
    if small + big == N - 1:
        result += 1
    
print(result)