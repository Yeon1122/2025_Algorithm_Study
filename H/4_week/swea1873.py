T = int(input())

dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
direction_map = {'U': '^', 'D': 'v', 'L': '<', 'R': '>'}
reverse_direction_map = {'^': 'U', 'v': 'D', '<': 'L', '>': 'R'}

def find_tank(origin_map, H, W):
    for x in range(H):
        for y in range(W):
            if origin_map[x][y] in ('^', 'v', '<', '>'):
                return x, y, reverse_direction_map[origin_map[x][y]]
    return None

def move_tank(x, y, d, origin_map, H, W):
    new_x, new_y = x + dx[d], y + dy[d]
    origin_map[x][y] = direction_map[d]  
    if 0 <= new_x < H and 0 <= new_y < W and origin_map[new_x][new_y] == '.':
        origin_map[new_x][new_y] = direction_map[d]
        origin_map[x][y] = '.'
        return new_x, new_y, d
    return x, y, d

def shoot(x, y, d, origin_map, H, W):
    bullet_x, bullet_y = x, y
    while True:
        bullet_x += dx[d]
        bullet_y += dy[d]
        if not (0 <= bullet_x < H and 0 <= bullet_y < W):  
            break
        if origin_map[bullet_x][bullet_y] == '*':
            origin_map[bullet_x][bullet_y] = '.'
            break
        if origin_map[bullet_x][bullet_y] == '#': 
            break

def play_game(H, W, origin_map, N_list):
    x, y, d = find_tank(origin_map, H, W)
    for command in N_list:
        if command in 'UDLR':
            x, y, d = move_tank(x, y, command, origin_map, H, W)
        elif command == 'S':
            shoot(x, y, d, origin_map, H, W)
    return origin_map

for tc in range(1, T + 1):
    H, W = map(int, input().split())
    origin_map = [list(input().strip()) for _ in range(H)]
    N = int(input())
    N_list = input().strip()
    
    result_map = play_game(H, W, origin_map, N_list)
    print(f"#{tc}")
    for row in result_map:
        print("".join(row))
