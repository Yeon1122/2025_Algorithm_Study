import sys
sys.setrecursionlimit(10**6)

N=int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
max_sum = 0

def dice(bottom,lst,k,sum):   #아랫면, 옆면의 최댓값 반환하는 함수
    if k == N:
        return sum

    if bottom==0: 
        sum+=max(lst[1],lst[2],lst[3],lst[4])   #옆면 중 최댓값 더해주기
        top=5    #다음 주사위의 아랫면 인덱스
    elif bottom==1:
        sum+=max(lst[0],lst[2],lst[4],lst[5])
        top=3
    elif bottom==2:
        sum+=max(lst[0],lst[1],lst[3],lst[5])
        top=4
    elif bottom==3:
        sum+=max(lst[0],lst[2],lst[4],lst[5])
        top=1
    elif bottom==4:
        sum+=max(lst[0],lst[1],lst[3],lst[5])
        top=2
    elif bottom==5:
        sum+=max(lst[1],lst[2],lst[3],lst[4])
        top=0   

    
    k+=1
    if k<N:
        next_bottom=arr[k].index(lst[top])
        return dice(next_bottom,arr[k],k,sum)
    else:
        return sum
    

for i in range(6):  #첫번째 주사위의 아랫면
    k=0
    sum=0
    sum6=dice(i,arr[k],k,sum)

    if sum6>max_sum:
        max_sum=sum6

print(max_sum)