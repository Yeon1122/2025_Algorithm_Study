#########################################
#
# #
#왼쪽 = 인덱스 번호 높이
# 기둥 개수
# 인덱스 번호, 높이
# 1. 높이 값을 리스트로 받고 싶은데 가장 큰 수 알 수 없음,
# 1-1. 딕셔너리 값으로 받아서 정렬, 키 값(인덱스)의 가장 큰 수 찾기 => 리스트 범위 찾기
#       높이 값 저장
#       [0]*키 값의 가장 큰 수
#       리스트 순회, 키 값(인덱스)에 맞춰서 값을 할당해주기(높이)
#
# 2. 높이 순회(지붕 만들어주기)
# 2-2. 직전 값 저장해주기(초기 값 = 0, 높은 것을 만나면 갱신),
#       지붕 = cnt. 직전 값보다 높을 때만 현재값-직전 값(=>초기값 0인 이유), 직전값 = 현재 값으로 갱신
#       직전값과 같거나 작으면 그냥 cnt+1, 한 칸 옆으로 넘어가기.
#       마지막 값=> 자기 높이 = 직전 값, cnt에 직전 값 더해주기#

N = int(input())
#1-1
ware_d = {}
for _ in range(N):
    a, b = map(int,input().split())
    ware_d[a] = b

# print(ware_d)
li_size = max(ware_d.keys())
li_start = min(ware_d.keys())
height = max(ware_d.values())
# print(li_size, li_start, height)

ware_li = [0]*(li_size+1)#li_size => 마지막 요소 인덱스 => +1

for key, value in ware_d.items():
    ware_li[key] = value

# print(ware_li)

#직전 값 초기 값
before = 0
#지붕 넓이
cnt = 0

max_idx = ware_li.index(height)
before = 0
for i in range(li_start, max_idx+1):
    if ware_li[i]>before:
        before = ware_li[i]
        cnt += before
        # print('b', before, ware_li[i], cnt)
        continue

    cnt += before
    # print('b', before, ware_li[i], cnt)

after = 0
for j in range(len(ware_li)-1, max_idx, -1):
    # print(j)
    if ware_li[j]>after:
        after = ware_li[j]
        # print('a', after, ware_li[j],cnt)
        cnt += after
        continue

    cnt += after
    # print('aa', after, ware_li[i], cnt)

print(cnt)
