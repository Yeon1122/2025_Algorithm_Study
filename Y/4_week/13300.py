N, K = map(int, input().split())
#성별에 맞춰서 학년 넣어주기
G = []
B = []

room_cnt = 0
for i in range(N):
    S, Y = map(int, input().split())
    #만약 성별이 0(여자)라면 Y를 리스트에 append
    if S == 0:
        G.append(Y)
    #0이 아니라면
    else:
        B.append(Y)

# print(N, K, G, B)

#방의 수 구하기 -> 각각 학년 수를 세주고 한 방에 들어갈 수 있는 최대 인원으로 나눈 몫, 만약 나머지가 있다면 +1
def room(k, li):
    global room_cnt
    st_count = [0] * 7
    #li를 순회 -> 각 학년당 얼마나 많은 사람이 있는지 카운트 해주기
    for i in li:
        st_count[i]+=1
    # print('cnt', st_count)
    #학년을 돌아주면서 계산해주기
    #1. 값이 0인 경우 넘어가기
    #2. (2-1)값이 0이 아니면서 (2-2) 값이 k(한 방에 들어갈 수 있는 최대 인원)로 나눴을 때 몫 = 방의 최소, 나머지가 있는 경우 몫+1
    for c in range(len(st_count)):
        if st_count[c] == 0:
            # print('co0', room_cnt, st_count[c])
            continue
        else:
            if st_count[c]%k == 0:
                room_cnt += st_count[c]//k
                # print('%0', room_cnt, st_count[c])
            else:
                room_cnt += (st_count[c]//k)+1
                # print(room_cnt, st_count[c])

    return room_cnt


result = room(K, G)
result = room(K, B)


print(result)