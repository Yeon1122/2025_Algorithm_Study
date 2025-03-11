def get_treasure_password(n, k, hex_string):
    unique_numbers = set()
    segment_length = n // 4
    hex_list = list(hex_string)
    for _ in range(segment_length):
        for i in range(4):
            start_idx = i * segment_length
            hex_number = ''.join(hex_list[start_idx:start_idx + segment_length])
            unique_numbers.add(int(hex_number, 16)) 
        hex_list.insert(0, hex_list.pop())
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[k - 1]
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    hex_string = input().strip() 
    result = get_treasure_password(N, K, hex_string)
    print(f"#{test_case} {result}")