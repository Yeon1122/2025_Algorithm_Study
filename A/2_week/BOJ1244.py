'''
남학생 : 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꿈 ==> 스위치 켜져 있으면 끄고 꺼져있으면 킨다.
ex) 3번을 받았으면 3,6을 바꿈

여학생 : 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우 대칭이면서 가장 많은 스위치 포함 구간을 찾아 다 바꿈 (모두 홀수)
if 좌우 대칭이면 다 바꾸고
else 아니라면 자기만 바꾼다

입력 :
1. 스위치 갯수 (N <= 100)
2. 스위치 상태
3. 학생 수
4. 학생의 상태 (status)
    > 1 3(남자 : 1 , 배정받은 번호 : 3)
    > 2 3(여자 : 2 , 배정받은 번호 : 3)


구조 )
반복문과 조건문을 돌며 계속 판단해야하는 것 같다.

30분
or 논리연산 완성 이후
>> 1시간 10분..
'''

N = int(input())
switch = list(map(int,input().split()))
student_num = int(input())
student = []
switch.insert(0,10) #이해 쉽게 인덱스 하나 추가
for i in range(student_num):
    a, b = map(int,input().split())
    c = (a,b)
    student.append(c)

for gen, num in student:
    if gen == 1:
        b = num
        while b <= N:
            switch[b] = 1 - switch[b]
            b += num

    elif gen == 2:
        i = 1
        switch[num] = 1 - switch[num]
        # 이 부분 빼도 될까?
        if num - i < 1 or num + i > N or switch[num - i] != switch[num + i]:
            switch[num] = 1 - switch[num]
        else:
            while (num - i) >= 1 and (num + i) <= N and switch[num-i] == switch[num+i]: # 인덱스 error 생각하면 앞에 범위값을 넣어주는게 나을듯
                switch[num - i] = 1 - switch[num - i]
                switch[num + i] = 1 - switch[num + i]
                i += 1

    else:
        break
switch.pop(0) # 추가해준 인덱스 지우기

for i in range(0,len(switch),20):
    print(*switch[i:i+20])