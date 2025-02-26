TC = int(input())
for tc in range(1, TC+1):
    N, *mission = map(str,input().split())

    B_next_aim = []
    O_next_aim = []
    B_loc = 1
    O_loc = 1
    result = 0

    for i in range(int(N)*2):
        if mission[i] == "B":
            B_next_aim.append(int(mission[i+1]))
        if mission[i] == "O":
            O_next_aim.append(int(mission[i+1]))
    
    while mission:
        result += 1

        if B_next_aim:
            if B_loc != B_next_aim[0]:
                if B_loc < B_next_aim[0]:
                    B_loc += 1
                else:
                    B_loc -= 1
            elif B_loc == B_next_aim[0] == int(mission[1]) and mission[0] == "B":
                B_next_aim.pop(0)
                mission.pop(0)
                mission.pop(0)
                if O_next_aim:
                    if O_loc == O_next_aim[0] == int(mission[1]) and mission[0] == "O":
                        continue

        if O_next_aim:
            if O_loc != O_next_aim[0]:
                if O_loc < O_next_aim[0]:
                    O_loc += 1
                else:
                    O_loc -= 1
            elif O_loc == O_next_aim[0] == int(mission[1]) and mission[0] == "O":
                O_next_aim.pop(0)
                mission.pop(0)
                mission.pop(0)

    print(f'#{tc} {result}')