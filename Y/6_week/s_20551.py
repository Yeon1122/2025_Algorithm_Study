T = int(input())
for test_case in range(1, T + 1):
    box = list(map(int, input().split()))
    cnt = 0
    for i in range(len(box) - 1):
        # print(i)
        for j in range(i + 1, len(box)):
            if box[i] < box[j]:
                continue
            else:
                while box[i] >= box[j]:
                    # print(box[i], i, box[j])
                    box[i] -= 1
                    cnt += 1

                    if i > 0:
                        if box[i] <= box[i - 1]:
                            while box[i] >= box[i - 1]:
                                # print(box[i], i, box[j])
                                box[i] -= 1
                                cnt += 1

                    if box[i] == 0:
                        cnt == 0
                        break

            if box[i] <= 0:
                cnt = -1
                break

    print(f'#{test_case} {cnt}')