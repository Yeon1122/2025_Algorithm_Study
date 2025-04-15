import sys
input=sys.stdin.readline

def solve(now,node):
    if node==0:
        return

    for n in arr[now]:
        if not visited[node][n]:
            visited[node][n]=1
            visited[n][node]=1
            solve(n,node)

N, M=map(int,input().split())
arr=[[] for _ in range(N+1)]
visited=[[0]*(N+1) for _ in range(N+1)]
result=0

for _ in range(M):
    a, b = map(int,input().split())
    arr[b].append(a)

for i in range(1,N+1):
    solve(i,i)

for lst in visited:
    cnt=lst.count(1)
    if cnt==N-1:
        result+=1
        
print(result)