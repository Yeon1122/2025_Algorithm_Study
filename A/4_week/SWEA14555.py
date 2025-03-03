'''
#입력 데이터
T : tc
S : 문자열

#구조
공은 무조건 () 하나의 세트

T
for tc
S = list(input())
ans = 0

for i <- len(S)
    if '(' == S[i]:
        if S[i+1] == | or S[i+1] == ')':
            cnt +=1

    if ')' == S[i] and S[i-1] == |:
        cnt +=1



'''
T = int(input())
for tc in range(1,T+1):
    S = list(input())
    ans = 0

    for i in range(len(S)):
        if '(' == S[i]:
            if S[i + 1] == '|' or S[i+1] == ')':
                ans += 1

        if ')' == S[i] and S[i - 1] == '|':
            ans += 1


    print(f'#{tc} {ans}')

