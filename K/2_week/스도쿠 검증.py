def check():

    for lst in arr:
        if len(set(lst)) != 9:
            return 0
    
    arr1=list(zip(*arr))
    for lst in arr1:
        if len(set(lst)) != 9:
            return 0
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            arr2=arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(arr2)) != 9:
                return 0
    return 1



T=int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    result = check()
    print(f'#{tc} {result}')
