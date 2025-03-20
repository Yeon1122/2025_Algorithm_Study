T=int(input())

def find(x):
    if boss[x]==x:
        return x
    ans=find(boss[x])
    boss[x]=ans
    return ans

def union(a,b):
    A=find(a)
    B=find(b)

    if A==B:
        return

    boss[B]=A

for tc in range(1,T+1):
    N, M=map(int,input().split())
    arr=list(map(int,input().split()))
    boss=list(range(N+1))

    for i in range(0,len(arr),2):
        union(arr[i],arr[i+1])

    result=set()
    for i in range(1,N+1):
        result.add(find(i))

    print(f'#{tc} {len(result)}')