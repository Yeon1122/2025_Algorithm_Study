'''
입력 :
수열 길이 N
수열 : list(map
증가할 때 카운트
감소할 때 카운트
카운트의 최대

구조)

while이나 for를 돌면서 확인하면 좋을 것 같은데,
for는 중간에 검사하기 힘들거 같아서 while로 해보는걸로
작아지는건지 커지는건지 확인을 해서 계속 넘어가는 식으로 해야하나?

3가지 경우를 생각해야 하는데,
1. 다음 리스트가 큰 경우 : max_cnt의 값을 올려준다 & min_cnt의 값을 초기화
2. 다음 리스트가 작은 경우 : min_cnt의 값을 올려준다 & max_cnt의 값을 초기화
3. 다음 리스트가 같은 경우 : 둘 다 하나 씩 올려준다.

'''

N = int(input())
lst = list(map(int,input().split()))

max_num = max_cnt = min_cnt = 1

for i in range(N-1):
    if lst[i] < lst[i+1]:
        max_cnt += 1
        min_cnt = 1
    elif lst[i] > lst[i+1]:
        min_cnt +=1
        max_cnt = 1
    else:   # 두 수가 같은 경우
        max_cnt += 1
        min_cnt += 1
    max_num = max(max_num, max_cnt, min_cnt) # max_num을 안 넣으면 어떻게 될까?

print(max_num)