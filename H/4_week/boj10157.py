def find_seat(C, R, K):
    # 격자 크기보다 K가 크면 불가능
    if K > C * R:
        return 0

    # 2차원 리스트(좌석) 생성
    grid = [[0] * C for _ in range(R)]

    # 방향 벡터 (위쪽 → 오른쪽 → 아래쪽 → 왼쪽)
    dr = [-1, 0, 1, 0]  # 행 변화 (위, 오른쪽, 아래, 왼쪽)
    dc = [0, 1, 0, -1]  # 열 변화 (위, 오른쪽, 아래, 왼쪽)
    
    # 초기 위치 설정
    row, col = R - 1, 0  # 시작 위치 (아래쪽 왼쪽)
    direction = 0  # 현재 방향 (0: 위쪽)
    
    for num in range(1, K + 1):
        grid[row][col] = num  # 현재 위치에 번호 배정

        # K번째 사람 찾았으면 반환
        if num == K:
            return (col + 1, R - row)  # 문제 요구사항에 맞게 좌표 변환

        # 다음 위치 계산
        nr, nc = row + dr[direction], col + dc[direction]

        # 범위를 벗어나거나 이미 값이 채워진 경우 → 방향 전환
        if not (0 <= nr < R and 0 <= nc < C) or grid[nr][nc] != 0:
            direction = (direction + 1) % 4  # 방향 변경
            nr, nc = row + dr[direction], col + dc[direction]  # 새로운 방향으로 이동
        
        # 위치 업데이트
        row, col = nr, nc

    return 0  # 실패할 경우

# 입력 받기
C, R = map(int, input().split())  # 가로 C, 세로 R
K = int(input())  # 대기번호

# 결과 출력
result = find_seat(C, R, K)
if result == 0:
    print(0)
else:
    print(result[0], result[1])  # x, y 좌표 출력
