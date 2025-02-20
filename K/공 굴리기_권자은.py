


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def ball(a,b):
    global count
    min_value=arr[a][b] #최솟값은 현재 인덱스값으로 초기화
    min_i,min_j=a,b #최솟값 인덱스는 현재 인덱스로 초기화


    for k in range(4):  #우 하 좌 상 탐색
        ni, nj = a+di[k], b +dj[k]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:  #우 하 좌 상이 N*N배열 벗어나면 안됨
            continue
        if arr[ni][nj]<min_value:   #이 방향의 값이 최솟값보다 작니
            min_value=arr[ni][nj]   #그렇다면 최솟값 갱신
            min_i,min_j=ni,nj   #그 최솟값 인덱스 갱신

    if min_value==arr[a][b]:    #4방향을 다 돌았는데 최솟값이 그대로니
        return count
    else:   #최솟값이 그대로가 아니면 한칸 이동한거니까 count+1
        count+=1

    ball(min_i,min_j)#최솟값 인덱스로 다시 쭉 이동해보자

    return count    #최종적으로 이동횟수를 리턴




T = int(input())
for tc in range(1,T+1):

    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]

    max_value=0

    for i in range(N):
        for j in range(N):
            count=1
            ball(i,j)

            if count>max_value:
                max_value=count
            count=0

    print(f'#{tc} {max_value}')
