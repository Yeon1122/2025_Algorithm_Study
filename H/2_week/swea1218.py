TC = 10
for tc in range(1, TC+1):
    N = int(input())
    list_tc = input()

    size = N
    stack = [0]*size
    top = -1

    result = 1                      # for문 돌때마다 변수값 초기화는 입력 안 받는 애들만 시켜주면 됨
    for x in list_tc:
        if x == '(' or x == '{' or x == '[' or x == '<':        # if x in "({[<":
            top += 1
            stack[top] = x
        elif x == ')' or x == '}' or x == ']' or x == '>':
            if top == -1:
                result = 0
                break
            else:
                # 괄호 종류별로 비교 작업
                if x == ')' and stack[top] == '(':
                    top -= 1
                elif x == '}' and stack[top] == '{':
                    top -= 1
                elif x == ']' and stack[top] == '[':
                    top -= 1
                elif x == '>' and stack[top] == '<':
                    top -= 1
                else:
                    result = 0
        else:
            result = 0

    if top > -1:
        result = 0

    print(f"#{tc} {result}")