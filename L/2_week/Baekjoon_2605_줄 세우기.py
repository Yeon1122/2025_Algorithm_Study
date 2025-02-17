# 줄 세우기

# [입력]
N = int(input()) #학생의 수
num = list(map(int,input().split())) #학생들이 뽑은 번호

# [처리]
# **변수**
result = [1] #첫번재 학생은 항상 0이니 일단 들어가 있는 것으로 초기값

# **식**
#학생들이 뽑은 번호를 돌면서(2번째 학생부터 끝까지) #한명씩 넣기
for i in range (1, N):
    pop_num = []

    #pop
    if num[i] > 0:
        for j in range(num[i]):
            pop_num.append(result.pop())
        
    #append
    #주인공 줄에 추가
    result.append(i+1)

    #잠시 빼둔 친구들 더하기
    if pop_num:
        pop_num.reverse()
        result += pop_num
        
# [출력]
for num in result:
    print(num, end=" ") #최종적으로 줄을 선 순서, 번호 사이 한 칸의 공백