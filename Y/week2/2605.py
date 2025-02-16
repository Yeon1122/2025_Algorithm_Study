N = int(input())
line = list(map(int, input().split()))
new_line = []
for i in range(N):
    new_line.insert(line[i], i+1)

lines = new_line[::-1]

print(*lines)
    
