T =int(input())
for tc in range(1,T+1):
 
    N,M=map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
 
    max_value=0
 
    def sum(a,b,m):
        sum=0
        for k in range(m):
            for l in range(m):
                sum+=arr[a+k][b+l]
        return sum
 
 
    for i in range(N-M+1):
        for j in range(N-M+1):
            if sum(i,j,M)>max_value:
                max_value=sum(i,j,M)
 
    print(f'#{tc} {max_value}')