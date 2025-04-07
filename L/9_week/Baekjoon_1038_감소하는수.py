N = int(input())

num_lst = [i for i in range(10)]

for num in num_lst:
    for i in range(10):
        if num%10 > i:
            new_num = num*10+i
            num_lst.append(new_num)

if N < len(num_lst):
    print(num_lst[N])
else:
    print(-1)