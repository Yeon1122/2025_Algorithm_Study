import sys

def solve(x,y):
    global result

    distance_F=abs(x-fx)+abs(y-fy)  #현재 위치에서 페스티벌까지의 거리
    if distance_F<=1000:    #1000미터 내로 갈 수 있는가?
        result='happy'
        return
    
    for i in range(N):
        distance_C=abs(x-c_position[i][0])+abs(y-c_position[i][1])  #현재 위치에서 각 편의점까지의 거리
        if distance_C>1000:  #1000미터보다 더 가야하면 패스
            continue
        if visited[i]:
            continue
        visited[i]=1
        solve(c_position[i][0],c_position[i][1])

    return
    
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    homex,homey=map(int,sys.stdin.readline().split())    #집 위치
    if N:   #편의점의 개수가 0이 아닐때
        c_position=[tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]  #각 편의점 위치를 튜플로 저장해서 리스트에 담음
    visited=[0]*N
    fx,fy=map(int,sys.stdin.readline().split())  #페스티벌 위치
    result='sad'

    solve(homex,homey)
    print(result)
    