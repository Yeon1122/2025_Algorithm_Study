T = int(input())
for tc in range(1, T+1):
    cnt = 0
    S = str(input())
    chars = list(S)
    
    for i in range(len(chars)):
        if i+1 < len(chars):
            if chars[i] == '(' and chars[i+1] == '|':
                cnt += 1
            elif chars[i] == '|' and chars[i+1] == ')':
                cnt += 1
            elif chars[i] == '(' and chars[i+1] == ')':
                cnt += 1

    print(f'#{tc} {cnt}')