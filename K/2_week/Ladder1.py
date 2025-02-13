for tc in range(10):
    tc=int(input())
 
    arr = [list(map(int,input().split()))+[0]for _ in range(100)]
    arrive_j=0 #도착점의 열 인덱스(나중에는 출발점의 X좌표)/행은 어차피 99니까 안구할거다
 
    for j in range(100): #도착점 찾기
        if arr[99][j]==2: #만약 인덱스의 값이 2면(도착점의 값) 해당 열의 인덱스값 저장
            arrive_j=j
 
    for i in range(99, -1, -1):    #행 99부터 0까지(한칸 한칸 올라가기)
         
        if arr[i][arrive_j-1]==1:   #왼쪽의 값이 1이면 실행
            while arr[i][arrive_j-1]==1:#왼쪽의 값이 0이 될때까지 실행행
                arrive_j-=1             #도착점의 열의 인덱스 값 -1
                 
        elif arr[i][arrive_j+1]==1: #오른쪽의 값이 1이면 실행
            while arr[i][arrive_j+1]==1:
                arrive_j+=1
         
    print(f'#{tc} {arrive_j}')