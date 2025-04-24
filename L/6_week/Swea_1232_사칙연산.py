T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)

    for i in range(N):
        lst = input().split()

        num = int(lst[0])

        if lst[1].isdigit():
            tree[num] = lst[1]
        else:
            tree[num] = lst[1]
            left[num] = int(lst[2])
            right[num] = int(lst[3])

    
    for j in range(N,0,-1):
        if not tree[j].isdigit():
            a = float(tree[left[j]])
            b = float(tree[right[j]])
            if tree[j] == '+':
                tree[j] = a + b
            if tree[j] == '-':
                tree[j] = a - b
            if tree[j] == '*':
                tree[j] = a * b
            if tree[j] == '/':
                tree[j] = a / b

    result = int(tree[1])

    print(f'#{tc} {result}')