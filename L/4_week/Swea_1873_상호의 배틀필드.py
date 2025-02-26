
def action(a):
    global loc_i
    global loc_j
    global head

    if a == "U":
        head = "^"
        gameboard[loc_i][loc_j] = head
        if 0 <= loc_i-1 < H:
            if gameboard[loc_i-1][loc_j] == ".":
                gameboard[loc_i][loc_j] = "."
                loc_i = loc_i-1           

    if a == "D":
        head = "v"
        gameboard[loc_i][loc_j] = head
        if 0 <= loc_i+1 < H: #gameboard[loc_i+1][loc_j]가 범위 안에 있고
            if gameboard[loc_i+1][loc_j] == ".":#gameboard[loc_i+1][loc_j]가 평지(.)이면
                gameboard[loc_i][loc_j] = "."#gamboard[loc_i][loc_j]가 평지이고,
                loc_i = loc_i+1
                

    if a == "L":
        head = "<"#head를 <로 바꾸고
        gameboard[loc_i][loc_j] = head
        if 0 <= loc_j-1 < W:#gameboard[loc_i][loc_j-1]가 범위 안에 있고
            if gameboard[loc_i][loc_j-1] == ".": #gameboard[loc_i][loc_j-1]가 평지(.)이면
                gameboard[loc_i][loc_j] = "." #gamboard[loc_i][loc_j]가 평지이고,
                loc_j = loc_j-1
                

    if a == "R":
        head = ">"#head를 >로 바꾸고
        gameboard[loc_i][loc_j] = head
        if 0 <= loc_j+1 < W: #gameboard[loc_i][loc_j+1]가 범위 안에 있고
            if gameboard[loc_i][loc_j+1] == ".": #gameboard[loc_i][loc_j+1]가 평지(.)이면
                gameboard[loc_i][loc_j] = "." #gamboard[loc_i][loc_j]가 평지이고,
                loc_j = loc_j+1
                

    if a == "S":
        temp_i = loc_i
        temp_j = loc_j
        
        if head == "^":
            while temp_i > 0:
                temp_i -= 1
                if gameboard[temp_i][temp_j] == "*":
                    gameboard[temp_i][temp_j] = "."
                    break
                if gameboard[temp_i][temp_j] == "#":
                    break

        if head == ">": #head가 >일때
            while temp_j < W-1:
                temp_j += 1
                if gameboard[temp_i][temp_j] == "*":
                    gameboard[temp_i][temp_j] = "."
                    break
                if gameboard[temp_i][temp_j] == "#":
                    break

        if head == "v":#head가 v일때
            while temp_i < H-1:
                temp_i += 1
                if gameboard[temp_i][temp_j] == "*":
                    gameboard[temp_i][temp_j] = "."
                    break
                if gameboard[temp_i][temp_j] == "#":
                    break

        if head == "<":#head가 <일때
            while temp_j > 0:
                temp_j -= 1
                if gameboard[temp_i][temp_j] == "*":
                    gameboard[temp_i][temp_j] = "."
                    break
                if gameboard[temp_i][temp_j] == "#":
                    break
    
    gameboard[loc_i][loc_j] = head


#[입력]
T = int(input()) #테스트 케이스의 수
for x in range(1,T+1): #T번 반복
    H, W = map(int,input().split()) #게임 맵의 높이, 너비
    gameboard = [list(map(str,input())) for _ in range(H)] #str로 된 list H개
    N = int(input()) #사용자가 넣을 입력의 개수
    inserts = list(map(str,input())) #str로 된 list 사용자가 넣은 입력

#[처리]
#변수
    loc_i = -1 #전차 위치점i
    loc_j = -1 #전차 위치점j
    head = "-" #전차방향

#식
#전체를 돌면서 전차가 있는 곳(^, v, <, >)을 찾아서 해당 좌표를 loc_i, loc_j, head로 두기
    for i in range(H):
        for j in range(W):
            if gameboard[i][j] in ["^", "v", "<", ">"]:
                loc_i, loc_j = i, j
                head = gameboard[i][j]
                # gameboard[i][j]= "."
                break

#Inserts를 돌면서 해당 Insert이면 실행하기
    for insert in inserts:
        action(insert)

    #[출력]
    print(f'#{x}', end=" ") # #테스트 케이스 번호
    for row in gameboard:
        print("".join(map(str,row))) #게임 맵