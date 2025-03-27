def comb(idx,cnt):
    global max_value
    
    if cnt==N-1:
        max_value=N
        return
    if idx==N:
        return
    
    for i in range(idx,N):
        if arr[i][0]>=meeting[-1][1]:
            meeting.append(arr[i])
            comb(idx+1,cnt+1)
            max_value=max(max_value,len(meeting))
            meeting.pop()

N=int(input())
arr=[]

for _ in range(N):
    a,b=map(int,input().split())
    arr.append((a,b))
arr.sort()

meeting=[]
meeting.append((0,0))
max_value=0

comb(0,0)

print(max_value-1)