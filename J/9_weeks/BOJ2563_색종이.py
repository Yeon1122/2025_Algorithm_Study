N = int(input())
paper = [[0]*102 for _ in range(102)]

for _ in range(N):
    R, C = map(int, input().split())
    for i in range(C, C+10):
        for j in range(R, R+10):
            paper[i][j] = 1

    visited = 0
    for cnt in paper:
        visited += sum(cnt)

print(visited)

