snow_d = []
for i in range(9):
    snow_d.append(int(input()))
sum_d = sum(snow_d)
two_d = sum_d-100

idx_i, idx_j = -1, -1

for i in range(0, len(snow_d)-1):
    for j in range(i+1, len(snow_d)):
        d_two = snow_d[i]+snow_d[j]
        if d_two == two_d:
            idx_i = i
            idx_j = j
            break

    if idx_i != -1:
        break

del snow_d[idx_j]
del snow_d[idx_i]

snow_d.sort()

for ans in snow_d:
    print(ans)