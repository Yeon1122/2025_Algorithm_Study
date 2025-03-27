import sys
input = sys.stdin.readline
N=int(input())
meeting=[tuple(map(int,input().split())) for _ in range(N)]

meeting.sort(key=lambda x :(x[1],x[0]))
end=meeting[0][1]
cnt=1

for s,e in meeting[1:]:
    if s>=end:
        cnt+=1
        end=e
print(cnt)