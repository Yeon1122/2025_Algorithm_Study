T = int(input())

def calculate(N, k, numbers):
    digits = [int(d) for d in str(N * k)]
    for i in range(len(digits)):
        numbers.update(digits)
    if len(numbers) == 10:
        return N * k
    else:
        return calculate(N, k+1, numbers)

for tc in range(1, T+1):
    N = int(input())
    numbers = set()
    result = calculate(N, 1, numbers)

    print(f'#{tc} {result}')