N = int(input())
room_list = [tuple(map(int,input().split())) for _ in range(N)]
room_list.sort()
max_num = 0
for i in range(N):
    max_num = max(max_num, max(room_list[i]))

dp_room = [[] for _ in range(N)]
dp_time = [0]*(max_num)

for i in range(N):
    start_time = room_list[i][0]
    end_time = room_list[i][1]
    if not dp_time[start_time]:

        dp_time[start_time] = max(dp_time) + 1

        for j in range(start_time, end_time):
                dp_time[j] = dp_time[start_time]
                for k in range(i+1, N):
                    if end_time > room_list[k][1]:
                        end_time = room_list[k][1]

                if j == end_time:
                    break
ans = max(dp_time)
print(ans)
