from collections import deque  # BFS 구현 시 사용할 deque
import copy  # lab(연구소 지도)를 복사해서 바이러스 퍼뜨릴 때 사용

# 1) 지도 크기 N(행), M(열) 입력 받기
N, M = map(int, input().split())

# 2) 연구소 지도를 2차원 리스트로 입력 받기
lab = [list(map(int, input().split())) for _ in range(N)]

# 3) 연구소에서 빈 칸(0)인 위치를 저장할 리스트
zero_lst = []

# 4) 연구소를 순회하면서 빈 칸(0) 위치만 zero_lst에 기록
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zero_lst.append((i, j))

# 5) 상, 하, 좌, 우 탐색을 위한 방향 벡터
di = [0, -1, 0, 1]
dj = [1,  0, -1, 0]

# 6) 최대 안전영역(0의 갯수) 결과를 저장할 변수
mx = 0

# ---------------------------------------------------------------------
# 함수: spread_virus()
# 목적: 
#   - 현재 연구소 지도(lab) 상태에서 바이러스를 퍼뜨린 후
#   - 안전영역(0의 갯수)을 계산하여 반환
# 절차:
#   1) lab를 deepcopy로 복사한다(바이러스 퍼뜨릴 때 원본 훼손 방지).
#   2) 복사한 지도에서 바이러스(2) 위치를 큐에 넣고 BFS 실행.
#   3) BFS로 2가 인접한 0을 2로 바꾼다(바이러스 전염).
#   4) 모든 전염 후 남아 있는 0의 갯수를 계산해 반환한다.
# ---------------------------------------------------------------------
def spread_virus():
    # lab를 깊은 복사(deepcopy)하여 copy_lab 생성
    copy_lab = copy.deepcopy(lab)
    q = deque()

    # 복사된 지도에서 바이러스(2) 위치를 큐에 저장
    for i in range(N):
        for j in range(M):
            if copy_lab[i][j] == 2:
                q.append((i, j))

    # 큐가 빌 때까지 BFS 수행
    while q:
        ci, cj = q.popleft()

        # 상하좌우로 탐색
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]

            # 지도 범위 안에 있고, 빈 칸(0)이면 바이러스로 전염(2로 변경)
            if 0 <= ni < N and 0 <= nj < M and copy_lab[ni][nj] == 0:
                copy_lab[ni][nj] = 2
                q.append((ni, nj))

    # 바이러스 전염이 끝난 뒤, 0(안전영역)의 개수를 세어 반환
    safe_zone = 0
    for i in range(N):
        for j in range(M):
            if copy_lab[i][j] == 0:
                safe_zone += 1
    return safe_zone

# ---------------------------------------------------------------------
# 함수: build_wall(wall, start)
# 목적: 
#   - 빈 칸(0)에 벽을 3개 세우는 모든 조합을 재귀적으로 시도
#   - 각 조합마다 spread_virus() 함수를 호출하여 안전영역 계산
#   - 최댓값(mx)을 갱신
# 매개변수:
#   - wall: 현재까지 세운 벽의 개수
#   - start: zero_lst에서 다음에 벽을 세울 수 있는 위치의 시작 인덱스
# ---------------------------------------------------------------------
def build_wall(wall, start):
    global mx
    # 벽을 3개 세운 경우, 바이러스 퍼뜨린 후 안전영역 계산
    if wall == 3:
        mx = max(mx, spread_virus())
        return

    # 아직 벽이 3개 미만인 경우, 남은 빈 칸에 벽을 세우는 모든 경우의 수 탐색
    for i in range(start, len(zero_lst)):
        x, y = zero_lst[i]
        # 벽 설치
        lab[x][y] = 1
        # 다음 벽 설치를 위해 재귀 호출 (wall+1, i+1)
        build_wall(wall + 1, i + 1)
        # 설치했던 벽을 다시 빈 칸(0)으로 되돌리기 (백트래킹)
        lab[x][y] = 0

# 7) build_wall 함수 최초 호출: 벽은 0개, zero_lst의 0번 인덱스부터 시작
build_wall(0, 0)

# 8) 최대로 확보할 수 있는 안전영역 크기를 출력
print(mx)
