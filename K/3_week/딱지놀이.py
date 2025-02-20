def c(arr_a,arr_b):
    i=4
    count=0
    while count==min_len:
        
        if arr_a.count(i)>arr_b.count(i):
            return 'A'
        elif arr_a.count(i)<arr_b.count(i):
            return 'B'
        
        count+=1
        i-=1
    return 0

N=int(input())
for tc in range(N):
    a, *arr_a=map(int,input().split())
    b, *arr_b=map(int,input().split())
    min_len=min(a, b)


    if c(arr_a,arr_b)==0:

        if a>b:
            print('A')
        elif a<b:
            print('B')
        elif a==b:
            print('D')
    else:
        print(c(arr_a,arr_b))
