T=int(input())
arr=[[0]*100 for _ in range(100)]
for tc in range(T):
    left, down=map(int,input().split())

    for i in range(left,left+10):
        for j in range(down,down+10):
            arr[i][j]=1

result=0
for lst in arr:
    result+=lst.count(1) 

print(result)