
import sys
sys.stdin = open(r"C:\Users\lhy98\OneDrive\바탕 화면\SSAFY_이하연\swea\input.txt", "r")

T = 10

for test_case in range(1, T+1):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i, sub_ladder in enumerate(ladder):
        for j, sub_ladder_2 in enumerate(sub_ladder):
            if sub_ladder_2 == 2:
                start = {"y" : i, "x": j}
                break

    while start["y"] != 0:
        if 0 <= start["x"] <= 99:
            #왼쪽으로 이동
            if start["x"] > 0:
                if ladder[start["y"]][start["x"]-1] == 1:
                    ladder[start["y"]][start["x"]-1] = 0
                    start["x"] = start["x"]-1

            #오른쪽으로 이동
            if start["x"] < 99:
                if ladder[start["y"]][start["x"]+1] == 1:
                    ladder[start["y"]][start["x"]+1] = 0
                    start["x"] = start["x"]+1

            #위로 이동
            if ladder[start["y"]-1][start["x"]] == 1:
                ladder[start["y"]-1][start["x"]] = 0
                start["y"] = start["y"]-1
        
            

    print(f'#{test_case} {start["x"]}')

#     최초 현재 방향 : 위

# while 도착때까지
#   # 방향 전환하는 상황
#   ㄱ. 위 > 좌 또는 우로 방향 전환 : 좌 또는 우 뚫려있으면
      
#   ㄴ. 좌 또는 우 > 위로 방향 전환 : 위가 뚫려있으면(0을 만나면)

# 위일 때는 좌>우>위 순으로 탐색