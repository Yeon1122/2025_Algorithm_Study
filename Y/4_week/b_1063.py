##################
# 킹의 위치K, 돌 위치 S
# 1.체스판이 있어야함
# 0 = 비어있는 체스판, 1 = 킹의 위치, 2 = 돌의 위치
# 2. 체스판 내에 킹, 돌의 위치를 알아내기
# 알파벳 = 딕셔너리를 활용해서 숫자로 변환하기
# -> 반복 코드 함수 사용, 
#   -> str을 받아서 받은 str의 앞과 뒤를 슬라이스
#   -> 앞(i)부분은 대응하는 딕셔너리(chess_alpha) 값으로 교체
#   -> (i,j)값 튜플로 리턴, chess에 1(왕) 또는 2(돌) 값을 구해두기#
# 3. 입력받은 움직임 값을 바탕으로 이동
# len(move)만큼 순회, 순회해서 얻은 값을 딕셔너리의 델타 값과 변경ni, nj#
#   a. 델타 값 범위 검사 
#   b. 다음 위치에 돌이 있다면 돌에도 같은 델타 값 적용
#       i) 돌 위치 델타 값 범위 검사
#       ii) 원래 돌 위치(= 킹의 위치) 1, 원래 킹의 위치는 0, 새로운 돌 위치에 2 적용
#       iii) 현재 킹 위치, 돌 위치 새로운 위치로 갱신
#       iiii) 범위 값 밖이면 다음 턴으로 넘기기(break)
#   c. 돌이 없으면 원래 킹의 위치 0, 새로운 킹 위치에 1, 위치 갱신해주기
# 
# 4. 출력 형식 바꿔주기
#   현재 [세로][가로]인데 출력값은 [가로][세로]임
#   ->뒤집어줘야함
#   현재 가로 값 = 숫자, 원래는 알파벳임. 변환했던 딕셔너리를 활용해서 다시 변환
#   => dict.items()를 활용해서 key, value를 추출해줘야함. value가 같을 때 key값으로 내용 전환
#   -> 변환 후 리스트를 뒤집고 문자열로 바꿔주기
#       a. for문을 활용해서 reverse = '' for c in list: c+reverse를 활용해서 뒤집기
#       b. list.reverse()를 활용, join(map(str, list))활용하기


###############################################################
K, S, N = input().split()
N = int(N)

#1.
chess = [[0]*9 for _ in range(9)]
chess_alpha = {'A':1, 'B':2,'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
move = []
move_delta = {
    'R' : (0, 1),
    'L' : (0, -1),
    'B' : (-1, 0),
    'T' : (1, 0),
    'RT' : (1, 1),
    'LT' : (1, -1),
    'RB' : (-1, 1),
    'LB' : (-1, -1)}

for _ in range(N):
    move.append(input())


#2. 왕의 위치, 돌의 위치 좌표값 알아내기, return 값은 튜플
def find_cur(str):
    ti = str[:1]
    tj = str[1:2]
    cur_i = chess_alpha[ti]
    cur_j = int(tj)

    return cur_j, cur_i 

king_cur = list(find_cur(K))
stone_cur = list(find_cur(S))

chess[king_cur[0]][king_cur[1]] = 1
chess[stone_cur[0]][stone_cur[1]] = 2


# 3. 입력값에 맞춰서 이동
for i in range(N):
    ni, nj = move_delta[move[i]]
    next_i = king_cur[0]+ni
    next_j = king_cur[1]+nj
    
    #틀린 이유 = 돌 델타 값을 확실하게 갱신해주지 않았음
    if 0<next_i<9 and 0<next_j<9:
        if chess[next_i][next_j] == 2:
            next_stone_i = stone_cur[0] + ni
            next_stone_j = stone_cur[1] + nj

            if 0<next_stone_i<9 and 0<next_stone_j<9:
                chess[king_cur[0]][king_cur[1]] = 0
                king_cur[0] = next_i
                king_cur[1] = next_j
                chess[king_cur[0]][king_cur[1]] = 1

                chess[stone_cur[0]][stone_cur[1]] = 0
                stone_cur[0] = next_stone_i
                stone_cur[1] = next_stone_j
                chess[stone_cur[0]][stone_cur[1]] = 2
            else:
                continue
        else:
            chess[king_cur[0]][king_cur[1]] = 0
            king_cur[0] = next_i
            king_cur[1] = next_j
            chess[king_cur[0]][king_cur[1]] = 1
    else:
        continue


#출력양식 변환
def chess_print(li):
    for k, v in chess_alpha.items():
        if v == li[1]:
            li[1] = k
    li.reverse()
    li_print = ''.join(map(str, li))
    return li_print

king_ans = chess_print(king_cur)
stone_ans = chess_print(stone_cur)

print(king_ans)
print(stone_ans)