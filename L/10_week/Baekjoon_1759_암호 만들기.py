'''
1759. 암호 만들기
[문제 이해]
사용했을 법한 문자의 종류 C가지
서로 다른 L개의 알파벳 소문자
- 최소 한 개의 모음(a, e, i, o, u)
- 최소 두 개의 자음
- 사전순

[입력]
L, C #비밀번호 자리 수, 비밀번호 후보 알파벳 수
letters #(리스트)비밀번호 후보 알파벳(C개)

[출력]
각 줄에 하나씩, 사전식으로 가능성 있는 암호들 모두 출력력

[문제 풀이]
조합 (CcL) - 중복 없는
조건 : 최소 한 개의 모음, 최소 두 개의 자음, 사전 순

1. 모든 경우의 수를 다 만들고 조건에 맞는 것만 answer에 더하기
2. 조건을 고려하면서 만들기 **더 쉬울 것 같아서 채택
'''

def comb(idx, answer):

    if len(answer) == L:
        #최소 한 개의 모음, 최소 두 개의 자음
        temp_v, temp_c = 0, 0
        for l in answer:
            if l in ['a','e','i','o','u']:
                temp_v += 1
            else:
                temp_c += 1
        
            if temp_v >= 1 and temp_c >= 2:
                print(''.join(answer))
                return
    
    for i in range(idx, C):
        comb(i+1,answer+[letters[i]])

L, C = map(int,input().split()) #비밀번호 자리 수, 비밀번호 후보 알파벳 수
letters = list(map(str,input().split())) #(리스트)비밀번호 후보 알파벳(C개)

#사전순
letters.sort()

comb(0,[])


'''
[배운점]
1. 조합 : 순서 상관없음, visited X / 순열 : 순서 중요, visited O
2. itertools 사용한 풀이
'''

#itertools 써서 조합 만들기기
from itertools import combinations

L, C = map(int, input().split())
letters = input().split()

letters.sort()  # 사전 순 정렬

vowels = {'a', 'e', 'i', 'o', 'u'}

for comb in combinations(letters, L):
    vowel_count = sum(1 for c in comb if c in vowels)
    consonant_count = L - vowel_count
    
    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(comb))
    
#조건을 충족하면서 조합 만들기기
def dfs(idx, path, vowel_count, consonant_count):
    if len(path) == L:
        if vowel_count >= 1 and consonant_count >= 2:
            print(''.join(path))
        return

    for i in range(idx, C):
        char = letters[i]
        if char in vowels:
            dfs(i + 1, path + [char], vowel_count + 1, consonant_count)
        else:
            dfs(i + 1, path + [char], vowel_count, consonant_count + 1)

# 입력 처리
L, C = map(int, input().split())
letters = input().split()
letters.sort()

vowels = {'a', 'e', 'i', 'o', 'u'}

dfs(0, [], 0, 0)


