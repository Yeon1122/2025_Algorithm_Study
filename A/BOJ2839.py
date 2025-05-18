'''
BOJ2839 설탕배달

# 입력
n : 배달해야 할 설탕 무게

# 구조
5kg 봉지를 최대한 많이 사용하고
남은 무게를 3kg 봉지로 채울 수 있는지 확인
불가능할 경우 3kg 봉지를 하나씩 늘려가며 반복
정확히 나눌 수 없는 경우 -1 출력


'''

n = int(input())

min_count = float('inf')

for x in range(n // 5 + 1):
    remaining = n - (5 * x)
    if remaining % 3 == 0:
        y = remaining // 3
        total = x + y
        min_count = min(min_count, total)

if min_count == float('inf'):
    print(-1)
else:
    print(min_count)
