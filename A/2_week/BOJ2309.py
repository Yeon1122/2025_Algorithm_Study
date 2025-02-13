'''
일곱난쟁이 문제


다 더해서 남는 수를 뺐을 때 100이 되어야 한다.


입력을 리스트로 받자.

구조:
1.리스트의 값을 모두 더한다.
2.그 값에서 100을 빼고 남은 수를 2중 for문을 이용해서 찾는다.
3.찾은 두 값을 빼주고, sort를 이용해서 출력

'''

dwarf = []

for i in range(9):
    a = int(input())
    dwarf.append(a)

fake_dwarf = sum(dwarf)-100
for i in range(9):
    if i == 8:
        break
    for j in range(i+1,9):
        if dwarf[i] + dwarf[j] == fake_dwarf:
            fake_1, fake_2 = i, j

dwarf1, dwarf2 = dwarf[fake_1], dwarf[fake_2]
dwarf.remove(dwarf1)
dwarf.remove(dwarf2)
dwarf.sort()

for i in range(7):
    print(dwarf[i])