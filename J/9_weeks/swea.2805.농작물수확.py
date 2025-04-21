def calc(l, r, op):
    if op == '+': return l + r
    elif op == '-': return l - r
    elif op == '*': return l * r
    elif op == '/': return l / r
 
def postorder(v):
    if tree[v][0] == 0 and tree[v][1] == 0: # 잎노드
        return tree[v][2]                   # 리턴(값)
    else: # 가지노드
        l = postorder(tree[v][0])       # l = postorder(왼쪽)
        r = postorder(tree[v][1])       # r = postorder(오른쪽)
        return calc(l, r, tree[v][2])   # return l 연산 r
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 정점수
    tree = [[0] * 3 for _ in range(N+1)]    # 고정된 인접리스트 (왼쪽, 오른쪽, 연산자나 값)
 
    for i in range(N):
        tmp = list(input().split())
        idx = int(tmp[0])  # 인덱스
        # 연산자일 때
        if tmp[1] == '+' or tmp[1] == '-' or tmp[1] == '*' or tmp[1] == '/':
            tree[idx][0] = int(tmp[2])   # 왼쪽자식
            tree[idx][1] = int(tmp[3])   # 오른쪽자식
            tree[idx][2] = tmp[1]       # 연산자
        else:               # 숫자(값)일 때
            tree[idx][2] = int(tmp[1])
 
    ans = postorder(1)
    print(f'#{tc} {int(ans)}')
