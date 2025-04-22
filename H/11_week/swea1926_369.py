N = int(input())
result = []

for i in range(1, N+1):
    cnt = 0
    for digit in str(i):
        if digit in '369':
            cnt += 1

    if cnt == 0:
        result.append(str(i))
    else:
        result.append('-' * cnt)

print(' '.join(result))