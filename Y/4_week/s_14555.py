T= int(input())
for test_case in range(1, T+1):
    bg = list(input())
    ball = 0
    for i in range(len(bg)-1):
        if bg[i] == '(' and bg[i+1] == '|':
            ball +=1
        elif bg[i] == '|' and bg[i+1] == ')':
        	ball += 1
        elif bg[i] == '(' and bg[i+1] == ')':
            ball += 1
            
            
    print(f'#{test_case} {ball}')