import heapq
N = int(input())
room_list = [tuple(map(int,input().split())) for _ in range(N)]
room_list.sort()

print(room_list)

dp_room = [[] for _ in range(N)]
dp_time = [0]*(N+1)

for i in range(N):
    if i == room_list[i][0]:
        for j in range(room_list[i][0], room_list[i][1]):
            if j<N:
                dp_room[j].append(i)


print(dp_room)

# end = room_list[0][1]
cnt = 0
# while cnt <= N:
#     if

flag = 0
# for i in range(N):

while cnt <=N:
    if cnt == room_list[cnt][0]:
        end = room_list[cnt][0]
        for j in range(room_list[cnt][1]):
            cnt += 1
            if j == room_list[j][0]:
                dp_time[cnt] +=1
                if room_list[j][1] < end:
                    end = room_list[j][1]
                    if j == end:
                        cnt = end
                        flag = 1
                        break
    if flag ==1:
        cnt += 1


    #
    #
    #
    #
    # if i == room_list[i][0]:
    #     for j in range(room_list[i][1]):
    #         dp_time[i]+=1
    #         end_time = room_list[i][1]
    #
    #     if i>0:
    #         if room_list[i][1]<end_time:
    #             end_time = room_list[i][1]
print()