# 스도쿠 검증 53분 23초

T = int(input())

for tc in range(1, T + 1):
    #s:스도쿠
    rc=[]
    #스도쿠 2차원 리스트로
    for i in range(9):
        s = input().split()
        rc.append(s)
    #배열 검증 1. 가로줄 2. 세로줄 3.9칸
    #1. 가로줄 테스트   #체크1의 모든 길이가 9이면. 가로줄 통과 아니면 break 후 check1이 0으로 할당당
    for i in range(9):
        if len(set(rc[i])) == 9:
            check1 = 1
        else:
            check1 = 0
            break
    #2 세로줄 테스트 일단 배열을 세로줄로 정렬해보기
    rc2=[]
    for i in range(9):
        mt = []
        for j in range(9):
            mt.append(rc[j][i])
        rc2.append(mt)
    #2 행렬 변환 하고 rc2에 넣고 1번과 똑같이 검증해보기
    for i in range(9):
        if len(set(rc2[i])) == 9:
            check2 = 1
        else:
            check2 = 0
            break    
    #3 9칸씩 묶기 // 이게 어차피 고정되어있는 애들이니까 하드코딩으로 묶을까? 아니면 다른 신박한 방법..
    rc3=[]
    for i in range(0,9,3):
        mt2=[]
        for j in range(3):
            mt2.extend(rc[i][j])
            mt2.extend(rc[i+1][j])
            mt2.extend(rc[i+2][j])
        rc3.append(mt2)
    for i in range(0,9,3):
        mt3=[]
        for j in range(3,6):
            mt3.append(rc[i][j])
            mt3.append(rc[i+1][j])
            mt3.append(rc[i+2][j])
        rc3.append(mt3)
    for i in range(0,9,3):
        mt4=[]
        for j in range(6,9):
            mt4.append(rc[i][j])
            mt4.append(rc[i+1][j])
            mt4.append(rc[i+2][j])
        rc3.append(mt4)
    # 9개씩 묶고 check3 생성
    for i in range(9):
        if len(set(rc3[i])) == 9:
            check3 = 1
        else:
            check3 = 0
            break
    if check1 and check2 and check3 == 1:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
    # print(rc3)



