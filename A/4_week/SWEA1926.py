'''
간단한 369게임
# 입력 데이터
N : 숫자 까지

# 구조
10이상, 100이하
100이상 1000이하



'''

N = int(input())
a = []

for i in range(1,N+1):
    a.append(str(i))

for i in a:
    if int(i) < 10:
        if i == '3' or i == '6' or i == '9':
            print('-',end=" ")
            continue
    if 10 <= int(i) < 100:
        if i[0] == '3' or i[0] == '6' or i[0] == '9':
            if i[1] == '3' or i[1] == '6' or i[1] == '9':
                print('--',end=" ")
                continue
            print('-', end=" ")
            continue
        if i[1] == '3' or i[1] == '6' or i[1] == '9':
            print('-', end=" ")
            continue
    if 100<= int(i) < 1000:
        if i[0] == '3' or i[0] == '6' or i[0] == '9':
            if i[1] == '3' or i[1] == '6' or i[1] == '9':
                if i[2] == '3' or i[2] == '6' or i[2] == '9':
                    print('---', end=" ")
                    continue
                print('--',end=" ")
                continue
            print('-', end=" ")
            continue
        if i[1] == '3' or i[1] == '6' or i[1] == '9':
            if i[2] == '3' or i[2] == '6' or i[2] == '9':
                print('--',end=" ")
                continue
            print('-', end=" ")
            continue
        if i[2] == '3' or i[2] == '6' or i[2] == '9':
            print('-', end=" ")
            continue


    print(i, end = " ")
