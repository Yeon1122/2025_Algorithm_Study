N = int(input())

time_li = [0]*N

for i in range(N):
    time_li[i] = list(map(int,input().split()))

time_li.sort(key=lambda x : (x[1],x[0]))

endtime = 0
answer = 0

for i in range(N):
    if time_li[i][0]>=endtime:
        answer += 1
        endtime = time_li[i][1]

print(answer)