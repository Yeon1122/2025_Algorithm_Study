from collections import deque

N, M, V = map(int, input().split())
adj_lst = [[] for _ in range(N+1)] #1,2,3,4 번 인덱스를 쓸거기 때문에 사용
visited = [0] * (N+1)

for i in range(M): # 무향이므로 양 쪽에 넣어주자
    a, b = map(int,input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

for i in range(1,N+1): # 인접 행렬에서 번호 작은거 먼저 탐색하기 위해서 sort해주자. 여기서 범위는
    adj_lst[i].sort()

# print(adj_lst) # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    for i in adj_lst[v]: # 행렬과는 다르게 [v]를 돌아줘야 할듯
        if not visited[i]:
            dfs(i)

def bfs(v):
    q = deque()
    print(v, end=" ")
    visited[v] = 2
    q.append(v)

    while q:
        cur = q.popleft()
        for i in adj_lst[cur]:
            if visited[i] == 1:
                print(i, end=" ")
                visited[i] = 2
                q.append(i)


dfs(V)
print()
bfs(V)
