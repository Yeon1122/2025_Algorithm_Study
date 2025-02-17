# [입력]
n_switch = int(input()) # 스위치의 개수
switch = list(map(int, input().split())) # 각 스위치의 상태
n_student = int(input()) # 학생 수
gender_number = [list(map(int, input().split())) for _ in range(n_student)] # 학생의 성별 / 학생이 받은 수
    
switch = [0] + switch

# [처리]

for gender, number in gender_number:
    if gender == 1:
        for j in range(number, n_switch + 1, number):
            switch[j] = 1 - switch[j]
    
    else:
        switch[number] = 1 - switch[number]
        k = 1
        while number-k > 0 and number+k <= n_switch and switch[number-k] == switch[number+k]:
            switch[number-k] = 1 - switch[number-k]
            switch[number+k] = 1 - switch[number+k]
            k += 1

# [출력]
#최종 스위치 상태
for i in range(1, n_switch+1, 20):
    print(*switch[i:i + 20])
    