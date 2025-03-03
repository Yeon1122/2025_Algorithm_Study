#########################
# 전역변수 T
# N = 배수를 하기 전 양의 수
# 
# 1. 숫자 0~9까지가 나올 때까지 반복
# -> while(몇 번 돌아야하는지 모름)
# -> 총 몇 번 돌았는지 세야함
# -> 몇 번 돌았는지 세 줄 수 있는 cnt가 필요함(int)
# 반복 시작 또는 끝에 cnt에 1을 더해줘서 다음 배수를 준비해야함
# 
# 2. 한 번 돌 때 어떤 숫자가 나왔는지 저장해야함
#   -> list가 필요
#   ->우선 N*cnt를 해주고 숫자를 순회하기
#   ->숫자는 반복 불가능 하기 때문에 str->int->list로 바꿔줘야함
#   ->숫자가 중복해서 존재할 수 있기 때문에 중복 검사도 해줘야함
#   ->set()을 사용하면 중복 제거가 가능
# 
# while의 기준
# flag 사용
# flag == 0일 때 반복
# 만약 리스트에 0~9까지 있을 때 flag가 1이 되도록 함
# 
# 0~9까지 판단하는 방법 
# 1번 방법 - set을 활용해서 0~9일때 = 길이가 10일때 멈추기
# 2번 방법 => 리스트 카운트 세주기? 
# => 숫자 - 인덱스 대응해서 순회했을 때 전부 1이 나오면 통과, cnt 출력
# #

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnt = 0
    sheep_list = []
    flag = 0

    while flag == 0:
        cnt += 1
        sheep = N*cnt
        sheep_num = list(map(int, str(sheep)))
        for i in range(len(sheep_num)):
            sheep_list.append(sheep_num[i])
        sheep_list = list(set(sheep_list))
        # print(sheep_list)
        if len(sheep_list) == 10:
            break
        else:
            continue

    print(f'#{test_case} {N*cnt}')