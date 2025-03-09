def show_tree(node):
    """ 후위 순회 방식으로 트리 출력 및 계산 """
    if node == 0:  # 자식이 없는 경우
        return

    show_tree(left[node])  # 왼쪽 자식 방문
    show_tree(right[node])  # 오른쪽 자식 방문

    if isinstance(tree[node], int):  # 숫자라면 스택에 push
        stack.append(tree[node])
    else:  # 연산자인 경우
        b = stack.pop()
        a = stack.pop()
        if tree[node] == '+':
            stack.append(a + b)
        elif tree[node] == '-':
            stack.append(a - b)
        elif tree[node] == '*':
            stack.append(a * b)
        elif tree[node] == '/':
            stack.append(a / b)  # 실수 연산

for tc in range(1, 11):
    result = 0
    N = int(input())  # 정점 개수
    tree = {}  # 노드 정보 저장

    left = [0] * (N + 1)  # 왼쪽 자식 저장
    right = [0] * (N + 1)  # 오른쪽 자식 저장

    for _ in range(N):
        data = input().split()
        node = int(data[0])

        if len(data) == 2:  # 숫자인 경우
            tree[node] = int(data[1])
        else:  # 연산자인 경우
            tree[node] = data[1]  # 연산자 저장
            left[node] = int(data[2])
            right[node] = int(data[3])

    stack = []  # 후위 순회하면서 사용할 스택
    show_tree(1)  # 루트(1번 노드)에서 시작하여 계산

    result = int(stack[0])  # 결과값 정수 변환 후 반환
    print(f"#{tc} {result}")

