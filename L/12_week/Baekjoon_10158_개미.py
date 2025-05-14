# di = [1,-1,1,-1] #우상 좌상 우하 좌하
# dj = [1,1,-1,-1]

# w,h = map(int,input().split())
# p,q = map(int,input().split())
# t = int(input())

# dir = 0

# for _ in range(t):
#     np = p + di[dir]
#     nq = q + dj[dir]

#     if np > w or np < 0:
#         if dir == 0:
#             dir = 1  # 우상 -> 좌상
#         elif dir == 1:
#             dir = 0  # 좌상 -> 우상
#         elif dir == 2:
#             dir = 3  # 우하 -> 좌하
#         elif dir == 3:
#             dir = 2  # 좌하 -> 우하


#     if nq > h or nq < 0:
#         if dir == 0:
#             dir = 2  # 우상 -> 우하
#         elif dir == 1:
#             dir = 3  # 좌상 -> 좌하
#         elif dir == 2:
#             dir = 0  # 우하 -> 우상
#         elif dir == 3:
#             dir = 1  # 좌하 -> 좌상

#     p += di[dir]
#     q += dj[dir]

# print(p,q)

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# x, y 좌표 계산
x = (p + t) % (2 * w)
y = (q + t) % (2 * h)

# 벽에 반사되는 처리
if x > w:
    x = 2 * w - x
if y > h:
    y = 2 * h - y

print(x, y)

