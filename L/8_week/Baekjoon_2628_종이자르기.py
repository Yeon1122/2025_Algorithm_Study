N, M = map(int,input().split())

#가로 길이 담기
lst1 = [[0,N]]

#세로 길이 담기
lst2 = [[0,M]]

K = int(input())
for _ in range(K):
    dir, num = map(int,input().split())
    #가로일 때
    if dir == 0:
        for c,d in lst2:
            if c<num and d>num:
                lst2.append([c,num])
                lst2.append([num,d])
                lst2.remove([c,d])
    #세로일 때
    else:
        for a,b in lst1:
            if a<num and b>num:
                lst1.append([a,num])
                lst1.append([num,b])
                lst1.remove([a,b])
    
# print("lst1",lst1)
# print("lst2",lst2)
#가장 긴 가로 찾기
result_a = 0
for a,b in lst1:
    result_a = max(result_a, b-a)

#가장 긴 세로 찾기
result_b = 0
for c,d in lst2:
    result_b = max(result_b, d-c)

#결과 구하기
# print("result_a",result_a)
# print("result_b",result_b)
result = result_a*result_b

print(result)


