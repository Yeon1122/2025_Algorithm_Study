T=int(input())

def calculate(cals_perm):
    global min_value, max_value
    ans=nums[0]
    
    for i in range(1,N):
        if cals[cals_perm[i-1]]==0:
            ans+= nums[i]
        elif cals[cals_perm[i-1]]==1:
            ans-= nums[i]
        elif cals[cals_perm[i-1]]==2:
            ans*= nums[i]
        elif cals[cals_perm[i-1]]==3:
            ans=int(ans/nums[i])
            
    min_value=min(min_value,ans)
    max_value=max(max_value,ans)


def perm(cnt):

    if cnt==len(cals):
        calculate(cals_perm)
        return
    
    for i in range(len(cals)):
        if not visited[i]:
            cals_perm.append(i)
            visited[i]=1
            perm(cnt+1)
            visited[i]=0
            cals_perm.pop()

for tc in range(1,T+1):
    N=int(input())
    cals_cnt=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    cals=[]
    min_value=float('inf')
    max_value=0

    for i in range(4):
        for _ in range(cals_cnt[i]):
            cals.append(i)

    cals_perm=[]
    visited=[0]*(len(cals))

    perm(0)

    result=max_value-min_value
    print(f'#{tc} {result}')