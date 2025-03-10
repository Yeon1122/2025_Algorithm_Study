# -입력-
# T : tc 수
# N : 학생 수
# ni, ti (N개) : 학생마다 현재 방 번호, 돌아가야 하는 방 번호
# corridor = 방 인덱스 [0] + 1 ~ 200 (총 201개)
# sn, en : 학생마다 현재, 목표 방 인덱스로 변환
# result = max(visited)

# -출력-
# f"#{tc} {result}"

# 1. tc 반복
# 2. N 입력받기
# 3. N 반복하면서 ni, ti 입력받기
# 	sn, en 인덱스로 변환
# 	corridor - visited 처리
# 4. result = max(corridor)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corridor = [0] * 201

    for _ in range(N):
        s, e = map(int, input().split())
        s, e = min(s, e), max(s, e)
        sn = (s + 1) // 2
        en = (e + 1) // 2

        for i in range(sn, en+1):
            corridor[i] += 1

    result = max(corridor)

    print(f"#{tc} {result}")
