n = int(input())
times = list(map(int, input().split()))

times.sort()

total = 0
acc = 0

for t in times:
    acc += t      # 지금까지의 누적 시간
    total += acc  # 각 사람의 대기 시간 총합

print(total)
