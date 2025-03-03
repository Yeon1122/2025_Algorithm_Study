
'''
#입력 데이터
N : 학생 수
K : 방 최대 인원 수
female, male
gen, grade : 성별 학년 데이터

#로직

1. 성별 분류
2. 학년 분류
3. %와 // 을 이용해 분류


'''

N, K = map(int,input().split())
female = []
male = []
rooms = 0
female_num = [0] * 7
male_num = [0] * 7
for _ in range(N):
    gen, grade = map(int,input().split())
    if gen == 0:
        female.append(grade)
    elif gen == 1:
        male.append(grade)

for i in range(len(female)):
    female_num[female[i]] += 1

for i in range(len(male)):
    male_num[male[i]] += 1

for i in range(1,7):
    if female_num[i]:
        rooms += female_num[i] // K
        if female_num[i] % K:
            rooms += 1
    if male_num[i]:
        rooms += male_num[i] // K
        if male_num[i] % K:
            rooms += 1

print(rooms)

