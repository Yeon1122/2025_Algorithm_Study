'''
필요 데이터

N
switches(리스트) 아무값
M

gender, number, idx
l, r

로직
1. N switches M 입력
2. M 줄에 걸쳐 gender number 입력
    ㄱ. 남자일 때
        - idx가 N 이하일 때까지 스위치 상태 변경 > idx += number
    
    ㄴ. 여자일 때
        a. l과 r 초기값 세팅
        b. 범위 안쪽일 때는 아래의 명령을 계속 반복
            - l과 r이 같은지 확인
                - 같을 때 > 스위치 상태 변경 > l과 r 갱신
                - 아닐 때 > break
3. 출력
    - 인덱스 1번부터 출력

'''

N = int(input())

switches = list(map(int, input().split()))
switches.insert(0, 0)
M = int(input())

for _ in range(M):
    gender, number = map(int, input().split())

    if gender == 1:
        idx = number

        while idx <= N:
            switches[idx] = (switches[idx]+1) % 2
            idx += number

        
    else:
        l = r = number
        while 1 <= l and r <= N:
            if switches[l]==switches[r]:                
                switches[l] = (switches[l]+1) % 2
                if l != r:
                    switches[r] = (switches[r]+1) % 2
                l -= 1
                r += 1

            else:
                break

    print(*switches[1:])