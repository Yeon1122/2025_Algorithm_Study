import heapq

def prim(start_node):
    pq=[(0,start_node)]
    MST=[0]*N
    min_cost=0

    while pq:
        cost, node=heapq.heappop(pq)

        if MST[node]:
            continue
        MST[node]=1
        min_cost+=cost

        for next_node in range(N):
            if MST[next_node]:
                continue

            heapq.heappush(pq,(weights[node][next_node],next_node))
    return min_cost

N=int(input())
nodes=[]
weights=[[0]*N for _ in range(N)]
for _ in range(N):
    x, y = map(float,input().split())
    nodes.append((x,y))

for i in range(N):
    for j in range(i+1,N):
        x,y=nodes[i]
        x2, y2=nodes[j]
        weight=((x-x2)**2+(y-y2)**2)**(1/2)
        weights[i][j]=weight
        weights[j][i]=weight

result=prim(0)
print(f'{result:.2f}')
