#dfs 함수
def dfs(i):
    global result
    
    if i == 99:
        result = 1
        return

    if first_arr[i]:
        dfs(first_arr[i])

    if second_arr[i]:
        dfs(second_arr[i])

#[입력]
T = 10 #총 10개의 테스트 케이스
for _ in range(1, T+1):
    t, L = map(int, input().split()) #t: 테스트 케이스의 번호 L: 길의 총 개수
    location = list(map(int, input().split()))

    first_arr = [0]*100
    second_arr = [0]*100
    result = 0

    for i in range(0, L*2, 2):
        if first_arr[location[i]] == 0:
            first_arr[location[i]] = location[i+1]
        elif second_arr[location[i]] == 0:
            second_arr[location[i]] = location[i+1]

    dfs(0)

    print(f'#{t} {result}')
