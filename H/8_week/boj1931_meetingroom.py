N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# meetings.sort(key = lambda x: (x[1], x[0])) 왜 안돌아가?????????????
def sort_key(x):
    return (x[1], x[0])

meetings.sort(key=sort_key)

cnt = 0
end_time = 0        # 마지막 끝난 시간

for start, end in meetings: # 현재 회의 시작, 종료시간
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)








# 경우마다 cnt 갱신하면서 max_cnt와 비교해 최댓값 계속 갱신시키기
