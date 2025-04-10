from collections import deque

def dfs(start_v):
    if visited[start_v]:
        return
    visited[start_v]=1
    print(start_v, end=' ')
    for i in range(N+1):
        if arr[start_v][i]:
            dfs(i)
            

def bfs(start_v):
    q=deque()
    q.append(start_v)
    bfs_result=[]
    while q:
        v=q.popleft()

        if visited[v]:
            continue
        visited[v]=1
        for i in range(1,N+1):
            if arr[v][i]==1:
                q.append(i)
        bfs_result.append(v)
    print(*bfs_result)


N, M, V=map(int,input().split())
arr=[[0]*(N+1) for _ in range(N+1)]
visited=[0]*(N+1)

for _ in range(M):
    a, b=map(int,input().split())
    arr[a][b]=1
    arr[b][a]=1

dfs(V)
visited=[0]*(N+1)
print()
bfs(V)