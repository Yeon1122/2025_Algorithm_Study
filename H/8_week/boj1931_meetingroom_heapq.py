import heapq

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

heap = []
for start, end in meetings:
    heapq.heappush(heap, (end, start))

count = 0
end_time = 0

while heap:
    end, start = heapq.heappop(heap)
    if start >= end_time:
        count += 1
        end_time = end

print(count)
