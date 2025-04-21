# def find_cm(cm):
    

# N = int(input())
# print(N)
# cm_list = []
# for _ in range(9):
#     cm_list.append(N)
#     cm_list.sort()
#     for i in range(0,N-1):
#         for j in range(i+1,N):
#             i+j = 32

def solve():
    num = sum(lst)-100
    for i in range(0,N-1):
        for j in range(i+1, N):
            if lst[i]+lst[j] == num:
                return lst[i], lst[j]

lst = [int(input()) for _ in range(9)]
n,m = solve()
for i in sored(lst):
    if i !- n and i != m:
        print(i)

