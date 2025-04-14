from itertools import combinations

L, C=map(int,input().split())
my_alp=list(map(str,input().split()))
my_alp.sort()

for code in combinations(my_alp,L):
    aeiou=False
    Jaeum=0
    for c in code:
        if c in 'aeiou':
            aeiou=True
        if c not in 'aeiou':
            Jaeum+=1
    if aeiou and Jaeum>=2:
        result=''.join(code)
        print(result)

#EASYYYYYYYY