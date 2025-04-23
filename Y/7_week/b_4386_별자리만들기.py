import heapq
from math import sqrt

def cal_dist(x, y, nx, ny):
    cal_ans = 0
    if x == nx and y!=ny:
        cal_ans = abs(ny-y)
    if y==ny and x!=nx:
        cal_ans = abs(nx-x)
    if x != nx and y != ny:
        # print('s')
        cal_ans = sqrt(abs((nx-x)**2 + (ny-y)**2))

    # print(cal_ans, 'a')
    return cal_ans


def prim(start_node):
    pq = [(0, start_node)]
    MST = [0]*(N+1)
    min_cost = 0
    while pq:
        cost, node = heapq.heappop(pq)
        if MST[node]:
            continue

        MST[node] = 1
        min_cost += cost

        for next_node in range(0, N):
            if not MST[next_node]:
                next_cost = cal_dist(star_pos[node][0], star_pos[node][1], star_pos[next_node][0], star_pos[next_node][1])
                heapq.heappush(pq, (next_cost, next_node))
    # print(node, MST)
    return round(min_cost, 2)
N = int(input())
star_pos = []
for i in range(N):
   star = tuple(map(float, input().split()))
   star_pos.append(star)
# print(star_pos)

print(prim(0))
