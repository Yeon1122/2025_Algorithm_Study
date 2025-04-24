def find_meeting(cnt,e):
    global answer
    temp_cnt = 0

    for ns, ne in meeting:
        if e <= ns:
            temp_cnt += 1
            # print("nextchoice",ns,ne)
            find_meeting(cnt+1,ne)

    if temp_cnt == 0:
        # print("end",cnt,ns,ne)
        answer = max(answer,cnt)
        return
    
N = int(input())
meeting = [list(map(int,input().split())) for _ in range(N)]
answer = 0

min_e = min(x for _,x in meeting)

for s, e in meeting:
    # print("Start",s,e)
    if s < min_e:
        find_meeting(1,e)

# for i in range(N):
#     for j in range(N):
#         if meeting[i][1] > meeting[j][0]:
#             find_meeting(1,meeting[j][1])

print(answer)