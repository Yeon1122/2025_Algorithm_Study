'''
[문제이해]
사각형 모형의 판, 얇은 치즈(회색-1), 판의 가장자리(치즈 X)
치즈에는 하나 이상의 구멍이 있을 수 있음
치즈를 공기 중에 놓으면 녹게 됨  ??? 왜 기화함
공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다
구멍이면 안 녹아없어짐

[입력]
N, M #사각형 모양 판의 세로, 가로
graph #(이중 리스트) M개 N줄

[출력]
모두 녹아 없어지는 시간
녹기 한 시간 전에 남아있는 치즈조각

[문제풀이]
좌표 나누기 : 구멍인 0 / 구멍이 아닌 0 / 치즈 1
치즈 1인 위치에서 bfs로 녹이기
조건: 구멍이 아닌 0에 인접해있음
'''
from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs():
    total_time = 0
    queue = deque([[0, 0]]) 
    while True:
        loc = set()
        while queue:
            r, c = queue.popleft()

            if graph[r][c]: 
                continue  

            for i in range(4):
                nr = r + di[i]
                nc = c + dj[i]

                if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]:
                    continue

                if graph[r][c] == 0 and graph[nr][nc]:  
                    loc.add((nr, nc))  

                if not graph[nr][nc]:  
                    visited[nr][nc] = 1 
                    queue.append([nr, nc])  

        if not len(loc): 
            return total_time

        for i in loc: 
            queue.append([i[0], i[1]])  
            visited[i[0]][i[1]] = 1  
            graph[i[0]][i[1]] = 0  

        total_time += 1 
        pre_cnt.append(len(loc))  

N, M = map(int,input().split()) 
graph = [list(map(int,input().split())) for _ in range(N)] 

visited = [[0] * M for _ in range(N)]
pre_cnt = []

print(bfs())
print(pre_cnt[-1])



