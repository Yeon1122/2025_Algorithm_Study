'''
입력 :
학생의 수
학생들이 뽑은 번호
학생들의 결과 리스트
학생들의 순서


구조
insert 함수를 써서 for문을 돌며 i 값을 넣는데,
학생들의 리스트 값이 변하니까 i만큼 뺴주면 그 앞으로 가게 될 듯


'''

N = int(input())
student = list(map(int, input().split()))
student_lst = []
stu_num = 1

for i in student:
    student_lst.insert(len(student_lst)-i, stu_num)
    stu_num += 1

ans = " ".join(map(str,student_lst))
print(ans)
