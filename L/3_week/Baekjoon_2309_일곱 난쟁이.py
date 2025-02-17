dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

for m in range(8):
    for n in range(m+1,9):
        if sum(dwarfs)-dwarfs[m]-dwarfs[n] == 100:
            result = [dwarfs[i] for i in range(9) if i != m and i !=n]
            break

result.sort()

for dwarf in result:
    print(dwarf)


